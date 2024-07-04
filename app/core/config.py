from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI MongoDB Project"
    MONGODB_URL: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()