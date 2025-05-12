import os
import shutil
from fastapi import FastAPI, File, UploadFile, WebSocket, WebSocketDisconnect
from back.transcribe import router as transcribe_router
from back.transcripts import router as transcripts_router
from back.websocket import websocket_endpoint
from back.summarize import router as summarize_router


app = FastAPI()

# Router'ları bağla
app.include_router(transcribe_router)
app.include_router(summarize_router)

app.include_router(transcripts_router)
app.websocket("/ws")(websocket_endpoint)



# WebSocket bağlantıları

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

    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"{file.filename} dosyası yüklendi"}

active_connections = []

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

# Bildirim fonksiyonu
