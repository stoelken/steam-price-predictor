import os
from dotenv import load_dotenv

def test_load_dotenv():
    load_dotenv()
    api_key = os.environ.get("STEAM_API_KEY")
    print(api_key)

test_load_dotenv()