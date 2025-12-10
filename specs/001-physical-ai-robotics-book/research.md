# Research Notes: Physical AI & Humanoid Robotics Book

**Date**: 2025-12-09
**Input**: `specs/001-physical-ai-robotics-book/spec.md`, `specs/001-physical-ai-robotics-book/plan.md`

## Overview

This `research.md` file documents the confirmed technology choices and design rationales for the "Physical AI & Humanoid Robotics Book" project. Based on the comprehensive `spec.md` and `plan.md`, no ambiguities or "NEEDS CLARIFICATION" items were found in the initial technical context. This document serves to consolidate the reasoning behind key architectural decisions.

## 1. Technology Stack Decisions

### 1.1 Frontend/Book: Docusaurus
- **Decision**: Docusaurus
- **Rationale**: Chosen for its suitability in building documentation websites, its Markdown-first approach, ease of customization, and strong community support. Aligns with the project goal of creating a "comprehensive, interactive online book".
- **Alternatives Considered**: Next.js, Gatsby (Docusaurus offers a more tailored solution for book-like content).

### 1.2 Backend API: FastAPI (Python)
- **Decision**: FastAPI
- **Rationale**: Selected for its high performance, ease of use for building APIs with Python, automatic interactive API documentation (Swagger UI/ReDoc), and strong type hinting support. Ideal for the RAG chatbot and user management backend.
- **Alternatives Considered**: Flask, Django (FastAPI provides a modern, high-performance solution with built-in API features).

### 1.3 AI/RAG Integration: OpenAI Agent SDK
- **Decision**: OpenAI Agent SDK
- **Rationale**: The project explicitly requires an integrated RAG chatbot. The OpenAI Agent SDK provides a robust framework for building AI agents, integrating with large language models, and managing tools for RAG.
- **Alternatives Considered**: LangChain (OpenAI Agent SDK is a direct fit for OpenAI's ecosystem).

### 1.4 Database: Neon Postgres
- **Decision**: Neon Postgres
- **Rationale**: Chosen for its serverless capabilities, auto-scaling, and compatibility with standard PostgreSQL. This offers a cost-effective and scalable solution for user profiles and logging data.
- **Alternatives Considered**: Supabase, traditional PostgreSQL hosting (Neon's serverless nature is a strong advantage for the target deployment environment).

### 1.5 Vector Store: Qdrant
- **Decision**: Qdrant
- **Rationale**: Selected as the vector database for storing vectorized book content. Qdrant is an open-source vector search engine known for its performance, scalability, and rich filtering capabilities, which are essential for efficient RAG operations.
- **Alternatives Considered**: Pinecone, Milvus (Qdrant's performance and open-source nature were key factors).

### 1.6 Authentication: BetterAuth
- **Decision**: BetterAuth
- **Rationale**: Explicitly chosen by the user and confirmed to be the standard for user authentication and personalization. Provides necessary features for signup, sign-in, and managing user profiles.
- **Alternatives Considered**: Auth0 (initially considered/mistakenly referenced, but BetterAuth is the confirmed choice).

### 1.7 Deployment: Vercel
- **Decision**: Vercel
- **Rationale**: Selected for its seamless deployment of both Docusaurus (frontend) and FastAPI (serverless functions), automatic scaling, and developer-friendly workflow, especially when integrated with GitHub.
- **Alternatives Considered**: Netlify, GitHub Pages, AWS Amplify (Vercel offers a strong, integrated platform for this specific stack).

## 2. Best Practices & Design Patterns

### 2.1 Monorepo Structure (`backend/` and `frontend/`)
- **Decision**: Adopt a `web + backend` monorepo structure.
- **Rationale**: This separation allows for independent development, testing, and deployment of the Docusaurus frontend and FastAPI backend. It promotes clear separation of concerns and facilitates team collaboration.

### 2.2 Observability (Metrics, Logging, Tracing)
- **Decision**: Implement detailed application metrics, structured logging, and distributed tracing.
- **Rationale**: Essential for monitoring application health, diagnosing issues, understanding performance bottlenecks, and ensuring reliability as specified in NFR-003.

### 2.3 Resilience (Retry Mechanisms, Circuit Breakers)
- **Decision**: Implement retry mechanisms with exponential backoff and circuit breakers for critical external services.
- **Rationale**: Directly addresses NFR-002, ensuring system reliability and graceful degradation when external dependencies (like OpenAI or Qdrant) experience transient failures or outages.

## 3. Unresolved Clarifications

No "NEEDS CLARIFICATION" items were identified in the `plan.md`'s Technical Context section, indicating a well-defined initial specification and plan. All core technology choices and architectural considerations are documented and understood.