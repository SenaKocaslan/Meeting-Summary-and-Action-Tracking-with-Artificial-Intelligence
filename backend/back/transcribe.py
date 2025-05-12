from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import whisper
import os
import psycopg2
from back.websocket import notify_clients


router = APIRouter()

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model("base")

    def db_connection(self):
        return psycopg2.connect(
            dbname="toplantidb",
            user="postgres",
            password="230565",
            host="localhost"
        )

    def transcribe_audio(self, path: str) -> str:
        result = self.model.transcribe(path, language="en")
        return result["text"]

    def save_to_db(self, filename: str, transcript: str):
        conn = self.db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO transkriptler (dosya_adi, transkript) VALUES (%s, %s)",
            (filename, transcript)
        )
        conn.commit()
        cur.close()
        conn.close()

transcriber = Transcriber()

@router.post("/transcribe")
async def transcribe_endpoint(file: UploadFile = File(...)):
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        text = transcriber.transcribe_audio(temp_path)
        transcriber.save_to_db(file.filename, text)
        os.remove(temp_path)
       
        await notify_clients("yeni_transkript")


        return JSONResponse(content={"status": "success", "message": "Transkript başarıyla kaydedildi."})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
