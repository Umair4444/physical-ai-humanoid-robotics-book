# Research Notes

This document contains research findings to address "NEEDS CLARIFICATION" points and establish best practices for the project.

## 1. BetterAuth Clarification

**Decision**: "BetterAuth" is a generic placeholder. The project will leverage **Auth0** for authentication, as it provides a robust, scalable, and widely-adopted solution that supports various integration methods suitable for both Docusaurus (frontend) and FastAPI (backend). It offers features like social logins, multi-factor authentication, and user management, aligning with the project's personalization and user profile requirements.

**Rationale**: Auth0 simplifies authentication implementation, reducing development time and security risks associated with building custom authentication systems. Its SDKs are well-maintained, and it integrates seamlessly with modern web frameworks.

**Alternatives Considered**:
- **Keycloak**: Open-source, powerful, but requires self-hosting and more complex management.
- **Firebase Authentication**: Good for simpler applications, but Auth0 offers more enterprise-grade features and flexibility for future scaling.
- **Custom OAuth/JWT**: High development effort, increased security risks, and ongoing maintenance burden.

## 2. Best Practices for Docusaurus with TypeScript and Reusable Components

**Decision**:
- **Setup**: Initialize Docusaurus with the official TypeScript template.
- **Project Structure**: Organize Docusaurus content (docs, blog, pages) in their respective directories. For custom React components, create a `src/components` directory within the Docusaurus project.
- **Styling**: Utilize Docusaurus's built-in theming capabilities, CSS modules, or Tailwind CSS for component styling to ensure consistency and maintainability.
- **Reusable Components**: Develop shared UI components (e.g., buttons, cards, specific chapter elements) as React components in TypeScript. These components will be importable and usable across various Docusaurus pages and MDX content.
- **Context7 Integration**: Docusaurus offers methods to extend markdown rendering. We will explore using MDX components or custom plugins to render Context7 documentation patterns.

**Rationale**: Following standard Docusaurus and React/TypeScript practices ensures maintainability, scalability, and leverages the strengths of the ecosystem. Reusable components promote consistency and accelerate development.

## 3. Best Practices for FastAPI with OpenAI-Agent SDK Integration

**Decision**:
- **FastAPI Setup**: Use a standard FastAPI project structure with routing, dependency injection for services, and Pydantic for data validation.
- **OpenAI-Agent SDK Integration**: Create a dedicated service layer within the FastAPI application to encapsulate all interactions with the OpenAI-Agent SDK. This service will handle agent initialization, tool registration (e.g., for RAG queries), and agent execution.
- **RAG Implementation**: The RAG logic will involve:
    1.  Pre-processing book content (Markdown to text chunks).
    2.  Embedding text chunks using an OpenAI embedding model.
    3.  Storing embeddings and metadata (chapter, section) in Qdrant.
    4.  At query time, embedding the user query, performing a similarity search in Qdrant, retrieving top-k relevant chunks.
    5.  Passing retrieved chunks as context to the OpenAI LLM via the Agent SDK.
- **Qdrant Connection**: Manage the Qdrant client as a singleton or via FastAPI's dependency injection system for efficient connection pooling.

**Rationale**: Separating concerns makes the codebase modular and testable. Leveraging Pydantic for API contracts ensures robust data handling. The Agent SDK provides a structured way to build AI applications, and Qdrant is optimized for vector similarity search.

## 4. Deployment Strategies for Docusaurus (Vercel/GitHub Pages) and FastAPI (Vercel Serverless)

**Decision**:
- **Primary Deployment (Vercel)**:
    - **Docusaurus Frontend**: Deploy Docusaurus directly to Vercel. Vercel automatically detects Docusaurus projects and configures build settings. Continuous deployment will be set up from the GitHub repository.
    - **FastAPI Backend**: Deploy FastAPI as serverless functions on Vercel. FastAPI endpoints will be served under the `/api` route. Vercel supports Python functions and handles scaling automatically.
- **Secondary Deployment (GitHub Pages)**:
    - **Docusaurus Frontend**: Configure GitHub Actions to build and deploy the Docusaurus site to GitHub Pages from the `main` branch. This will serve as a reliable backup or alternative for the static book content.
    - **FastAPI Backend**: GitHub Pages does *not* support dynamic backend services. For a GitHub Pages deployment, the FastAPI backend would need to be deployed separately (e.g., on a different cloud provider or a dedicated server) and the Docusaurus frontend configured to point to that external API. *This will be noted as a significant architectural difference for GitHub Pages deployment.*

**Rationale**: Vercel offers a seamless developer experience with integrated frontend and backend deployment, automatic scaling, and custom domain support. GitHub Pages provides a free, simple hosting solution for static content, suitable as a secondary option for the book itself.

## 5. Integration of Neon PostgreSQL with FastAPI

**Decision**:
- **ORM**: Use **SQLModel** (built on Pydantic and SQLAlchemy) for database interactions. SQLModel provides a type-safe way to define models and perform CRUD operations, integrating well with FastAPI's Pydantic models.
- **Connection Management**: Utilize FastAPI's dependency injection for database sessions, ensuring that connections are properly managed and closed after each request.
- **Neon-Specifics**: Configure SQLModel to connect to the Neon PostgreSQL instance using the provided connection string. Leverage Neon's branching capabilities for development/staging environments if needed.

**Rationale**: SQLModel provides a modern, type-safe, and FastAPI-idiomatic approach to database access. Dependency injection ensures efficient and correct handling of database sessions. Neon offers a serverless PostgreSQL experience with good scalability and branching features.

## 6. Recommended Testing Frameworks

**Decision**:
- **FastAPI (Backend)**:
    - **Unit/Integration Tests**: `pytest` with `httpx` for API testing and `pytest-asyncio` for asynchronous tests. `SQLAlchemy`'s test utilities for database interaction testing.
    - **Mocks**: `unittest.mock` for isolating components during testing.
- **Docusaurus (Frontend)**:
    - **Unit Tests (React Components)**: `Jest` and `React Testing Library` for testing individual React components.
    - **End-to-End (E2E) Tests**: `Playwright` for simulating user interactions across the Docusaurus site, covering navigation, RAG chatbot interaction, and personalization features.

**Rationale**: These frameworks are widely adopted, well-documented, and provide comprehensive features for robust testing across the full stack. They align with best practices for Python and JavaScript ecosystems.