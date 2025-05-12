from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()

class Summarizer:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    async def summarize_text(self, text: str) -> str:
        print("Özetlenecek metin:", text)

        prompt = f"Bu metni özetle:\n\n{text}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.url,
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=60
                )
            print("Ollama yanıtı:", response.text)


            if response.status_code == 200:
                data = response.json()
                return data.get("response", "").strip()
            else:
                raise HTTPException(status_code=response.status_code, detail="Özetleme hatası")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ollama hatası: {str(e)}")

summarizer = Summarizer()

@router.post("/summarize")
async def summarize(request: Request):
    try:
        body = await request.json()
        text = body.get("text")

        if not text:
            raise HTTPException(status_code=400, detail="Metin eksik")

        summary = await summarizer.summarize_text(text)
        return JSONResponse(content={"summary": summary})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
