from fastapi import FastAPI
from websocket import router as websocket_router

app = FastAPI()

# WebSocket endpoint'ini FastAPI'ye ekle
app.include_router(websocket_router)
