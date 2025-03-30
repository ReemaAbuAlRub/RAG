import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Config, cls).__new__(cls)
            cls.instance.initialize()
        return cls.instance
    
    def initialize(self):
        self.api_key = os.getenv("API_KEY", "")
        self.model=os.getenv("MODEL", "")
        self.base_url=os.getenv("BASE_URL", "")

config = Config()