import os
from dotenv import load_dotenv

def load_api_key() -> str:
    load_dotenv()
    api_key = os.getenv("EIA_API_KEY")
    if not api_key:
        raise ValueError("EIA_API_KEY is not set. Add it to .env or export it in the environment.")
    return api_key