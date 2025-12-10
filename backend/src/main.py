from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.rag import router as rag_router # Import the rag router
from backend.src.api.auth import auth_router # Import the auth router
from backend.src.api.users import users_router # Import the users router

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
app.include_router(auth_router, prefix="/auth", tags=["Authentication"]) # Added auth router
app.include_router(users_router, prefix="/users", tags=["Users"]) # Added users router
