
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def test_reddit_connection():
    """Otestuje připojení k Reddit API"""
    
    print("🔄 Připojuji se k Reddit API...")
    
    try:
        # Vytvoření Reddit instance
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        
        # Test: Získáme informace o read-only režimu
        print(f"✅ Připojení úspěšné!")
        print(f"   Read-only mode: {reddit.read_only}")
        
        # Test: Získáme pár příspěvků z r/python jako test
        print("\n🔍 Testuji získání dat...")
        subreddit = reddit.subreddit("python")
        print(f"   Subreddit: r/{subreddit.display_name}")
        print(f"   Počet členů: {subreddit.subscribers:,}")
        
        # Získáme 3 top příspěvky jako test
        print("\n📝 Top 3 příspěvky z r/python:")
        for i, post in enumerate(subreddit.hot(limit=3), 1):
            print(f"   {i}. {post.title[:60]}...")
            print(f"      👍 {post.score} | 💬 {post.num_comments} komentářů")
        
        print("\n✅ Vše funguje perfektně! Můžeme pokračovat.")
        return True
        
    except Exception as e:
        print(f"\n❌ Chyba při připojení: {e}")
        print("\n🔧 Zkontrolujte:")
        print("   1. Máte správně vyplněný .env soubor?")
        print("   2. Jsou REDDIT_CLIENT_ID a REDDIT_CLIENT_SECRET správné?")
        print("   3. Jste připojeni k internetu?")
        return False

if __name__ == "__main__":
    test_reddit_connection()
