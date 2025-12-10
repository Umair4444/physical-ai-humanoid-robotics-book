from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.rag import router as rag_router # Import the rag router

app = FastAPI(
    title="Physical AI & Humanoid Robotics Book Backend",
    description="FastAPI backend for RAG chatbot and user management.",
    version="0.1.0",
)

# CORS Middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Book Backend!"}

# Include routers
app.include_router(rag_router, prefix="/rag", tags=["RAG Chatbot"])
