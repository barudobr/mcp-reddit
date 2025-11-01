"""
Reddit MCP Server - ZJEDNODUŠENÁ VERZE
"""

from reddit_tools import RedditTools
import json

# Vytvoření instance Reddit Tools
reddit_tools = RedditTools()


def get_subreddit_posts(subreddit_name: str, limit: int = 10, sort_by: str = "hot"):
    """Získá příspěvky ze subredditu"""
    posts = reddit_tools.get_subreddit_posts(subreddit_name, limit, sort_by)
    return json.dumps(posts, indent=2, ensure_ascii=False)


def search_reddit(query: str, subreddit_name: str = None, limit: int = 10, sort_by: str = "relevance"):
    """Vyhledá na Redditu"""
    results = reddit_tools.search_reddit(query, subreddit_name, limit, sort_by)
    return json.dumps(results, indent=2, ensure_ascii=False)


def get_post_comments(post_id: str, limit: int = None):
    """Získá komentáře k příspěvku"""
    comments = reddit_tools.get_post_comments(post_id, limit)
    return json.dumps(comments, indent=2, ensure_ascii=False)


def get_subreddit_info(subreddit_name: str):
    """Získá info o subredditu"""
    info = reddit_tools.get_subreddit_info(subreddit_name)
    return json.dumps(info, indent=2, ensure_ascii=False)


def get_user_info(username: str):
    """Získá info o uživateli"""
    info = reddit_tools.get_user_info(username)
    return json.dumps(info, indent=2, ensure_ascii=False)


def analyze_posts_sentiment(subreddit_name: str = None, search_query: str = None, limit: int = 50):
    """Analyzuje sentiment příspěvků"""
    if search_query:
        posts = reddit_tools.search_reddit(search_query, subreddit_name, limit)
    elif subreddit_name:
        posts = reddit_tools.get_subreddit_posts(subreddit_name, limit)
    else:
        return json.dumps({"error": "Musíte zadat subreddit_name nebo search_query"}, indent=2)
    
    sentiment = reddit_tools.analyze_sentiment(posts)
    return json.dumps(sentiment, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    print("🚀 Reddit MCP Server - Testovací režim")
    print("\n📝 Test: Získání příspěvků z r/python")
    result = get_subreddit_posts("python", limit=3)
    print(result[:500] + "...")
    
    print("\n✅ Server je připraven!")