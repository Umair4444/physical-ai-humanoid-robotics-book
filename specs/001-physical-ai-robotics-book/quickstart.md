# Quickstart Guide

This guide provides instructions to quickly set up and run the "Physical AI & Humanoid Robotics" book project locally.

## Prerequisites

Ensure you have the following installed on your system:

-   **Git**: For cloning the repository.
-   **Python 3.9+**: For the FastAPI backend.
-   **Node.js (LTS recommended)**: For the Docusaurus frontend.
-   **npm** or **Yarn**: Node.js package manager (npm comes with Node.js).
-   **Docker** (Optional, for local Qdrant instance): If you don't use a hosted Qdrant service.
-   **Auth0 Account**: For user authentication.
-   **Neon PostgreSQL Account**: For the database.
-   **OpenAI API Key**: For the OpenAI Agent SDK.
-   **Qdrant Instance**: Either a hosted service or a local Docker container.

## 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/The-Ummah/physical-ai-humanoid-robotics-book.git
cd physical-ai-humanoid-robotics-book
```

## 2. Environment Setup

Create a `.env` file in the root of the project for environment variables. This file should NOT be committed to version control.

```
# Auth0 Configuration
AUTH0_DOMAIN=your_auth0_domain.auth0.com
AUTH0_API_AUDIENCE=your_auth0_api_audience
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
AUTH0_CALLBACK_URL=http://localhost:3000/callback

# Neon PostgreSQL Configuration
DATABASE_URL="postgresql://user:password@host:port/database"

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# Qdrant Configuration
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_API_KEY=your_qdrant_api_key (if using a hosted Qdrant)
QDRANT_COLLECTION_NAME=book_chapters
```

Replace the placeholder values with your actual credentials.

## 3. Backend Setup (FastAPI)

Navigate to the `backend` directory, create a Python virtual environment, install dependencies, and apply database migrations.

```bash
cd backend
python -m venv venv
./venv/Scripts/activate  # On Windows
# source venv/bin/activate # On Linux/macOS

pip install -r requirements.txt
# If using SQLModel for migrations, typically:
# alembic upgrade head
```

## 4. Run the Backend (FastAPI)

Start the FastAPI application.

```bash
uvicorn main:app --reload --port 8000
```

The backend API will be available at `http://localhost:8000`.

## 5. Frontend Setup (Docusaurus)

Open a new terminal, navigate to the `frontend` directory, and install Node.js dependencies.

```bash
cd ../frontend
npm install # or yarn install
```

## 6. Run the Frontend (Docusaurus)

Start the Docusaurus development server.

```bash
npm start # or yarn start
```

The Docusaurus book will be available at `http://localhost:3000`.

## 7. Vectorize Book Content (for RAG)

Before using the RAG chatbot, you need to vectorize the book content and upload it to Qdrant. This usually involves a separate script.

```bash
# Example (actual script name/location may vary)
python scripts/vectorize_content.py
```

Ensure your Qdrant instance is running and accessible (e.g., via Docker: `docker run -p 6333:6333 qdrant/qdrant`).

---

**Note**: Refer to the `README.md` in both `backend/` and `frontend/` directories for more detailed, project-specific setup and development instructions.