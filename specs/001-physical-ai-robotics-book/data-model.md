# Data Model

This document outlines the key entities, their attributes, relationships, and validation rules based on the feature specification.

## 1. User Profile

Represents a registered user in the system. Stored in Neon PostgreSQL.

-   **Entity**: `User`
-   **Table Name**: `users`
-   **Attributes**:
    -   `user_id` (UUID, Primary Key): Unique identifier for the user.
    -   `auth_provider_id` (String, Unique): ID from the authentication provider (Auth0).
    -   `email` (String, Unique): User's email address.
    -   `profile_data` (JSONB): A JSON object containing additional user-specific details.
-   **`profile_data` Structure**:
    -   `background_sw` (String): User's software background (e.g., "Student", "Professional", "Beginner", "Intermediate", "Advanced").
    -   `background_hw` (String): User's hardware background (e.g., "Student", "Professional", "Beginner", "Intermediate", "Advanced").
    -   `preferences` (JSONB): A JSON object for personalization settings.
        -   `translation_language` (String, default: "en"): Currently supports "en" (English) and "ur" (Urdu).
        -   `chapter_order` (Array of Strings): Ordered list of chapter IDs for personalized display.
        -   `hidden_chapters` (Array of Strings): List of chapter IDs the user wishes to hide.
        -   `highlighted_chapters` (Array of Strings): List of chapter IDs the user wishes to highlight.
-   **Relationships**: One-to-many with `RAGLog` (a user can have many RAG interactions).
-   **Validation Rules**:
    -   `email` must be a valid email format.
    -   `background_sw` and `background_hw` must be from a predefined set of values.
    -   `translation_language` must be "en" or "ur".

## 2. RAG Log

Records user interactions with the RAG chatbot. Stored in Neon PostgreSQL.

-   **Entity**: `RAGLog`
-   **Table Name**: `rag_logs`
-   **Attributes**:
    -   `log_id` (UUID, Primary Key): Unique identifier for the log entry.
    -   `user_id` (UUID, Foreign Key, Nullable): References `User.user_id`. Null if the user is not signed in.
    -   `query_text` (Text): The question asked by the user.
    -   `response_text` (Text): The answer provided by the chatbot.
    -   `query_mode` (String): "full-book" or "selected-text".
    -   `source_chapter` (String, Nullable): Chapter from which the response was primarily sourced.
    -   `source_url` (String, Nullable): URL to the source section in the book.
    -   `timestamp` (Timestamp with timezone): When the interaction occurred.
-   **Relationships**: Many-to-one with `User` (many logs can belong to one user).
-   **Validation Rules**:
    -   `query_mode` must be "full-book" or "selected-text".
    -   `query_text` and `response_text` cannot be empty.

## 3. Chapter Content Vector

Represents vectorized chunks of the book's content for RAG. Stored in Qdrant.

-   **Entity**: `ChapterContentVector`
-   **Collection Name**: `book_chapters` (in Qdrant)
-   **Attributes (Payload in Qdrant)**:
    -   `id` (String): Unique identifier for the text chunk (e.g., `module-chapter-chunk_index`).
    -   `vector` (Vector): The numerical embedding of the text chunk.
    -   `content` (Text): The raw text of the chunk.
    -   `module` (String): The module the chunk belongs to (e.g., "Module 1").
    -   `chapter_title` (String): The title of the chapter.
    -   `chapter_id` (String): Unique identifier for the chapter (e.g., "1.1").
    -   `url` (String): Relative URL to the specific section or chapter in Docusaurus.
    -   `last_updated` (Timestamp with timezone): When the vector was last generated/updated.
-   **Relationships**: None directly within Qdrant, but logically linked to the Docusaurus book content.
-   **Validation Rules**:
    -   `vector` must be of a consistent dimension.
    -   `content`, `module`, `chapter_title`, `chapter_id`, `url` cannot be empty.
    -   `id` must be unique.