import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API = os.getenv('API_KEY')
