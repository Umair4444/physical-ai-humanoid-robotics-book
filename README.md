# Physical AI & Humanoid Robotics Book

This repository contains the codebase for the "Physical AI & Humanoid Robotics Book", an interactive online book featuring a RAG chatbot and user personalization. The project consists of a Docusaurus-based frontend and a FastAPI backend.

## Project Structure

- `frontend/`: Contains the Docusaurus frontend application.
- `backend/`: Contains the FastAPI backend application.
- `.github/workflows/`: GitHub Actions for CI/CD.
- `specs/`: Project specifications, plans, and tasks.

## Getting Started

### Prerequisites

Ensure you have the following installed:

-   **Git**
-   **Python 3.11+**
-   **uv** (Python package installer): `pip install uv`
-   **Node.js LTS** (recommended via `nvm`)

### 1. Clone the Repository

```bash
git clone https://github.com/The-Ummah/physical-ai-humanoid-robotics-book.git
cd physical-ai-humanoid-robotics-book
```

### 2. Backend Setup (FastAPI)

Navigate to the `backend` directory, install dependencies, and run the application:

```bash
cd backend
uv sync
uv run main.py --reload # For local development with auto-reloading
```

#### Backend Environment Variables (`backend/.env`)

Create a `.env` file in the `backend/` directory with the following variables:

-   `DATABASE_URL`: Connection string for Neon Postgres (e.g., `postgresql+asyncpg://user:password@host:port/database`).
-   `QDRANT_URL`: URL for your Qdrant instance.
-   `OPENAI_API_KEY`: API key for OpenAI Agent SDK.
-   `BETTERAUTH_CLIENT_ID`: Client ID for BetterAuth.
-   `BETTERAUTH_CLIENT_SECRET`: Client Secret for BetterAuth.
-   `BETTERAUTH_DOMAIN`: Domain for BetterAuth.
-   `SECRET_KEY`: A strong, random key for JWT token signing (e.g., generated with `openssl rand -hex 32`).
-   `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for access tokens in minutes (e.g., `30`).

### 3. Frontend Setup (Docusaurus)

Open a new terminal, navigate to the `frontend` directory, install dependencies, and start the Docusaurus development server:

```bash
cd frontend
npm install
npm start
```

The Docusaurus book should be accessible in your browser, typically at `http://localhost:3000`.

#### Frontend Environment Variables (`frontend/.env`)

(Note: Docusaurus usually consumes environment variables prefixed with `DOCUSAURUS_` or `GATSBY_` or similar during build time, and may require specific handling for runtime variables. For client-side secrets, proxy through the backend or use a secure, non-exposed method.)

-   `REACT_APP_BACKEND_URL`: URL of the backend API (e.g., `http://localhost:8000` or your Vercel deployment URL).
-   `REACT_APP_BETTERAUTH_DOMAIN`: Your BetterAuth domain.
-   `REACT_APP_BETTERAUTH_CLIENT_ID`: Your BetterAuth client ID.

## Deployment

This project is configured for deployment with Vercel. A `vercel.json` file is provided at the root of the repository to configure both the frontend and backend deployments as serverless functions.

### Vercel Commands

-   **Deploy**: `vercel`
-   **Deploy to Production**: `vercel --prod`

## Contributing

Please refer to the [Project Constitution](/.specify/memory/constitution.md) for detailed contribution guidelines, including branch naming conventions, Conventional Commits, and Pull Request processes.
