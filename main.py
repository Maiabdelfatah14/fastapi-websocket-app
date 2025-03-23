import os
import asyncio
import json
import random
import uvicorn
import jwt
import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import Optional

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_jwt_token(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.websocket("/ws/auth")
async def websocket_auth(websocket: WebSocket):
    await websocket.accept()
    try:
        token = await websocket.receive_text()  # Receive token from client
        user_id = verify_jwt(token)  # Validate token
        await websocket.send_text(f"Welcome {user_id}, token verified successfully!")
    except HTTPException as e:
        await websocket.send_text(str(e.detail))
        await websocket.close(code=1008)  # Close connection on authentication failure

connected_clients = set()
clients_lock = asyncio.Lock()  # Lock to protect concurrent operations
stocks = ["AAPL", "GOOGL", "AMZN", "MSFT"]

@app.websocket("/ws/stocks")
async def websocket_stocks(websocket: WebSocket):
    await websocket.accept()
    try:
        token = await websocket.receive_text()  # Receive token from client
        user_id = verify_jwt(token)  # Validate token
        await websocket.send_text(f"Welcome {user_id}, connected to stock updates.")

        async with clients_lock:
            connected_clients.add(websocket)
        
        while True:
            async with clients_lock:
                if connected_clients:
                    stock_data = {stock: round(random.uniform(100, 1500), 2) for stock in stocks}
                    message = json.dumps(stock_data)
                    await asyncio.gather(*(client.send_text(message) for client in connected_clients))
            await asyncio.sleep(2)
    except (WebSocketDisconnect, HTTPException):
        async with clients_lock:
            connected_clients.discard(websocket)
        await websocket.close(code=1008)

@app.get("/")
async def health_check():
    return {"status": "healthy"}

@app.get("/crash")
async def crash():
    raise HTTPException(status_code=500, detail="Simulated server crash error")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
