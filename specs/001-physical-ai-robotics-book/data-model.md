# Data Model: Physical AI & Humanoid Robotics Book

**Date**: 2025-12-09
**Input**: `specs/001-physical-ai-robotics-book/spec.md`, `.specify/memory/constitution.md`

## 1. Overview

This document defines the key entities and their relationships for the "Physical AI & Humanoid Robotics Book" project. It consolidates information from the feature specification (`spec.md`) and the project constitution (`constitution.md`) to establish a clear data model.

## 2. Key Entities

### 2.1 User Profile

Represents a registered user of the system.

-   **Description**: Stores user identification, authentication provider link, and personalization settings.
-   **Source**: `spec.md` (Key Entities), `constitution.md` (Minimal Schema Rules)
-   **Fields**:
    *   `user_id` (UUID, Primary Key): Unique identifier for the user.
    *   `auth_provider_id` (String): Identifier from the BetterAuth provider.
    *   `full_name` (String, Optional): User's full name.
    *   `email` (String, Unique): User's email address.
    *   `registration_date` (DateTime): Timestamp of user registration.
    *   `last_login_date` (DateTime): Timestamp of the user's last login.
    *   `profile_data` (JSONB): A JSON object containing additional profile information.
        *   `background_sw` (String): User's software background (e.g., "student", "professional").
        *   `background_hw` (String): User's hardware background (e.g., "beginner", "expert").
        *   `preferences` (JSONB): User's personalization preferences (e.g., `{"translation_language": "Urdu", "chapter_order": [...]}`).
-   **Relationships**: Linked to `RAG Log` (one-to-many).
-   **Validation Rules**:
    *   `email` must be a valid email format.
    *   `auth_provider_id` must be present for authenticated users.

### 2.2 RAG Log

Records user interactions with the RAG chatbot.

-   **Description**: Stores the user's query, the chatbot's response, and a reference to the user if logged in.
-   **Source**: `spec.md` (Key Entities)
-   **Fields**:
    *   `log_id` (UUID, Primary Key): Unique identifier for the log entry.
    *   `user_id` (UUID, Foreign Key, Optional): References `User Profile.user_id` if the user is signed in.
    *   `query_text` (Text): The question asked by the user.
    *   `response_text` (Text): The answer provided by the chatbot.
    *   `source_chapter` (String, Optional): Reference to the chapter(s) used for the response.
    *   `source_url` (String, Optional): URL to the relevant section in the book.
    *   `timestamp` (DateTime): Timestamp of the query/response.
    *   `mode` (String): "full-book" or "selected-text".
-   **Relationships**: Many-to-one with `User Profile`.

### 2.3 Chapter Vector

Vectorized representation of book content for semantic search.

-   **Description**: Stores embedding vectors of text chunks from the book, used by Qdrant for RAG.
-   **Source**: `spec.md` (Key Entities)
-   **Fields**:
    *   `vector_id` (UUID, Primary Key, Qdrant internal): Unique identifier for the vector.
    *   `chapter_id` (String): Identifier for the chapter (e.g., "module-1-chapter-1-1").
    *   `text_chunk` (Text): The original text segment that was vectorized.
    *   `embedding` (Vector): The numerical vector representation of `text_chunk`.
    *   `metadata` (JSONB, Optional): Additional metadata like section, page number, etc.
-   **Storage**: Qdrant (vector store).
-   **Validation Rules**: PII must be explicitly excluded from vectorization (`constitution.md`).

## 3. Relationships

-   **User Profile to RAG Log**: One `User Profile` can have many `RAG Log` entries. An `RAG Log` entry can optionally belong to one `User Profile`.

## 4. Storage Locations

-   **User Profile, RAG Log**: Neon Postgres
-   **Chapter Vector**: Qdrant

## 5. Potential State Transitions (User Profile)

-   **Unregistered User** -> **Registered User**: Via signup process.
-   **Registered User** -> **Logged In User**: Via sign-in process.
-   **Logged In User** -> **Logged Out User**: Via sign-out action.
-   **User Profile Update**: Changes to `full_name`, `email`, `background_sw`, `background_hw`, `preferences`.