import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "reddit-mcp-actor/1.0")

def validate_config():
    if not REDDIT_CLIENT_ID:
        raise ValueError("REDDIT_CLIENT_ID není nastavené v .env souboru!")
    if not REDDIT_CLIENT_SECRET:
        raise ValueError("REDDIT_CLIENT_SECRET není nastavené v .env souboru!")
    
    print("✅ Konfigurace načtena úspěšně!")
    print(f"   Client ID: {REDDIT_CLIENT_ID[:8]}...")
    print(f"   User Agent: {REDDIT_USER_AGENT}")
    
    return True

if __name__ == "__main__":
    validate_config()