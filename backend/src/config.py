from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str
    QDRANT_URL: str
    OPENAI_API_KEY: str
    BETTERAUTH_CLIENT_ID: str
    BETTERAUTH_CLIENT_SECRET: str
    BETTERAUTH_DOMAIN: str

settings = Settings()
