from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
from fastapi.responses import JSONResponse
import whisper
import psycopg2
from fastapi import WebSocket, WebSocketDisconnect
from typing import List


app = FastAPI()
model = whisper.load_model("base")



def db_connection():
    return psycopg2.connect(
        dbname= "toplantidb",
        user= "postgres",
        password= "230565",
        host= "localhost"
    )

@app.get("/")
def hello():
    return {"message": "Merhaba"}


@app.get("/uploads")
def list_uploaded_files():
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        return {"files": []}
    
    files = os.listdir(upload_dir)
    return {"files": files}

@app.post("/uploads")
async def upload_audio(file: UploadFile = File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path= os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {"message" : f"{file.filename} dosyasi yuklendi"}



@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
   try:
       temp_path = f"temp_{file.filename}"

       with open(temp_path, "wb") as buffer:
           buffer.write(await file.read())

        

       result = model.transcribe(temp_path, language="en")
       transcript = result["text"]

       conn = db_connection()
       cur = conn.cursor()
       cur.execute(
           "INSERT INTO transkriptler (dosya_adi, transkript) VALUES (%s, %s)",
           (file.filename, transcript)
       )

       conn.commit()
       cur.close()
       conn.close()

       os.remove(temp_path)

       return JSONResponse(content={"status": "success", "message": "Transkript başarıyla kaydedildi."})
   
   except Exception as e:
       return JSONResponse(status_code=500, content={"error":str(e)})


@app.get("/transcripts")
def get_transcripts():
    try:
        conn= db_connection()
        cur= conn.cursor()
        
        cur.execute("SELECT id, dosya_adi, transkript FROM transkriptler ORDER BY id DESC")
        rows= cur.fetchall()

        cur.close()
        conn.close()

        transcripts = []
        for row in rows:
            transcripts.append({
                "id": row[0],
                "dosya_adi": row[1],
                "transkript": row[2]
            })  

        return {"transkript": transcripts}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})





# Bağlı istemcileri tutmak için liste
active_connections: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    print("WebSocket bağlandı")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Alınan mesaj: {data}")
            await websocket.send_text(f"Sunucu yanıtı: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print("WebSocket bağlantısı kesildi")

# Transkript oluşturulduğunda istemcilere haber veren fonksiyon
async def notify_clients(message: str):
    disconnected_clients = []
    for connection in active_connections:
        try:
            await connection.send_text(message)
        except WebSocketDisconnect:
            disconnected_clients.append(connection)
    for dc in disconnected_clients:
        active_connections.remove(dc)
