from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow our Chrome extension to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Project Owl Backend is running 🦉"
    }

@app.get("/analyze")
def analyze():
    return {
        "decision": "BUY",
        "score": 9.2,
        "reason": "This is a demo response from Project Owl."
    }