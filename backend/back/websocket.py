# websocket_handler.py

from fastapi import WebSocket, WebSocketDisconnect
from typing import List

active_connections: List[WebSocket] = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    print("WebSocket bağlandı")

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Sunucu yanıtı: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print("WebSocket bağlantısı kesildi")

async def notify_clients(message: str):
    disconnected = []
    for conn in active_connections:
        try:
            await conn.send_text(message)
        except WebSocketDisconnect:
            disconnected.append(conn)
    for dc in disconnected:
        active_connections.remove(dc)
