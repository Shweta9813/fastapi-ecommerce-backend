import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env', override=True, verbose=True)

class Settings:
    def init__(self):
        self.MONGO_URI: str = self._get_env("MONGO_URI")
        self.JWT_SECRET_KEY: str = self._get_env("JWT_SECRET_KEY")
        self.JWT_ALGORITHM: str = self._get_env("JWT_ALGORITHM")
        self.JWT_EXPIRE_MINUTES: int = int(self._get_env("JWT_EXPIRE_MINUTES", "60"))

    def _get_env(self, key: str, default: str= None) -> str:
        value = os.getenv(key, default)
        if value is None or value.strip() == "":
            raise EnvironmentError(f"Environment variable '{key}' is not set or is empty.")
        return value
    
settings = Settings()