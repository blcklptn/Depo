from pydantic import BaseSettings
from dotenv import load_dotenv



class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str

settings = Settings()
