# Quickstart Guide: Physical AI & Humanoid Robotics Book

**Date**: 2025-12-09
**Input**: `specs/001-physical-ai-robotics-book/spec.md`, `specs/001-physical-ai-robotics-book/plan.md`, `.specify/memory/constitution.md`

## 1. Introduction

This guide provides a quick overview of how to set up and run the "Physical AI & Humanoid Robotics Book" project locally. The project consists of a Docusaurus-based frontend for the book content and a FastAPI backend for the RAG chatbot and user management.

## 2. Prerequisites

Ensure you have the following software installed on your system:

-   **Git**: For cloning the repository.
-   **Python 3.11+**: For the FastAPI backend.
-   **uv**: A fast Python package installer and resolver.
    ```bash
    pip install uv
    ```
-   **Node.js LTS**: For the Docusaurus frontend. We recommend using `nvm` (Node Version Manager) to manage Node.js versions.

## 3. Getting Started

### 3.1 Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/The-Ummah/physical-ai-humanoid-robotics-book.git
cd physical-ai-humanoid-robotics-book
```

### 3.2 Backend Setup (FastAPI)

Navigate to the `backend` directory, install dependencies using `uv`, and run the application:

```bash
cd backend
uv sync
uv run app.py  # Or appropriate entry point for FastAPI
```

### 3.3 Frontend Setup (Docusaurus)

Open a new terminal, navigate to the `frontend` directory, install dependencies, and start the Docusaurus development server:

```bash
cd frontend
npm install
npm start
```

The Docusaurus book should now be accessible in your browser, typically at `http://localhost:3000`.

## 4. Environment Variables

Both the frontend and backend require environment variables for configuration (e.g., API keys, database connection strings). Refer to the `.env.example` files in both the `frontend/` and `backend/` directories for a list of required variables.

**Important**: Never commit your `.env` files to Git.

## 5. Contributing

This project adheres to strict contribution guidelines outlined in the [Project Constitution](/.specify/memory/constitution.md). Key points include:

-   **Branch Naming**: All branches MUST follow conventions like `feature/[description]`.
-   **Commits**: Adhere to the Conventional Commits specification.
-   **Pull Requests (PRs)**: All changes to `main` MUST go through a PR and require at least one approving review.
-   **Mandatory Push Rule**: After every logical unit of work, especially after creating a Prompt History Record (PHR) or completing a feature task, the full repository state MUST be committed and pushed to its feature branch.

Please review the full [Project Constitution](/.specify/memory/constitution.md) for detailed guidelines before contributing.