from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

connected_clients = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Gelen veri: {data}")
            # Gelen veriyi tüm kullanıcılara gönder
            for client in connected_clients:
                await client.send_text(f"AI cevabı: {data.upper()}")  # örnek cevap
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Kullanıcı bağlantısı koptu.")

