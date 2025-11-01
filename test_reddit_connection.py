
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def test_reddit_connection():
  
    
    print("Connection to Reddit API...")
    
    try:
     
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        
        print(f"Succesfull connection")
        print(f"   Read-only mode: {reddit.read_only}")
       
        print("\n Getting data testint")
        subreddit = reddit.subreddit("python")
        print(f"   Subreddit: r/{subreddit.display_name}")
        print(f"   Number of subscribers: {subreddit.subscribers:,}")
       
        print("\nTop 3 posts from r/python:")
        for i, post in enumerate(subreddit.hot(limit=3), 1):
            print(f"   {i}. {post.title[:60]}...")
            print(f"    {post.score} | 💬 {post.num_comments} comments")
        
        print("\nEverything works.")
        return True
        
    except Exception as e:
        print(f"\nError when connecting: {e}")
        print("\nCheck:")
        print("   1. Is the .env file properly configured?")
        print("   2. Are REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET correct?")
        print("   3. Is the internet connection working?")
        return False

if __name__ == "__main__":
    test_reddit_connection()
