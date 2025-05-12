from fastapi import APIRouter
from fastapi.responses import JSONResponse
import psycopg2

router = APIRouter()

class TranscriptManager:
    def __init__(self):
        self.db_config = {
            "dbname": "toplantidb",
            "user": "postgres",
            "password": "230565",
            "host": "localhost"
        }

    def db_connection(self):
        return psycopg2.connect(**self.db_config)

    def fetch_all_transcripts(self):
        try:
            conn = self.db_connection()
            cur = conn.cursor()
            cur.execute("SELECT id, dosya_adi, transkript FROM transkriptler ORDER BY id DESC")
            rows = cur.fetchall()
            cur.close()
            conn.close()

            transcripts = []
            for row in rows:
                transcripts.append({
                    "id": row[0],
                    "dosya_adi": row[1],
                    "transkript": row[2]
                })

            return transcripts
        except Exception as e:
            raise e

manager = TranscriptManager()

@router.get("/transcripts")
def get_transcripts():
    try:
        transcripts = manager.fetch_all_transcripts()
        return {"transkript": transcripts}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
