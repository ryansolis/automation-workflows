from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
#import os
from dotenv import load_dotenv
from fastapi import WebSocket

# Load environment variables for local development
load_dotenv()

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("WebSocket connection established!")
    await websocket.close()

# Load workflows
#WORKFLOW_FILE = os.path.join(os.path.dirname(__file__), "workflows.json")

#try:
#    with open(WORKFLOW_FILE, "r") as f:
#        workflows = json.load(f)
#except FileNotFoundError:
#    workflows = {"error": "Workflows file not found"}
# Load workflows
with open("backend/workflows.json", "r") as f:
    workflows = json.load(f)

@app.get("/api/workflows")
def get_workflows():
    return workflows

if __name__ == "__main__":
    import uvicorn
    # HOST = os.getenv("HOST", "0.0.0.0")
    # PORT = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="127.0.0.1", port=8000)
