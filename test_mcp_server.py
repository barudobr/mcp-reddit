

from reddit_tools import RedditTools
import json


def test_reddit_functions():
    
    
    tools = RedditTools()
    
    print("=" * 60)
    print("🧪 TESTOVÁNÍ REDDIT FUNKCÍ")
    print("=" * 60)
    
    # Test 1: Získání příspěvků
    print("\n📝 TEST 1: Získání příspěvků z r/python")
    print("-" * 60)
    posts = tools.get_subreddit_posts("python", limit=3, sort_by="hot")
    
    if isinstance(posts, list):
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title'][:60]}...")
            print(f"   👍 {post['score']} | 💬 {post['num_comments']} komentářů")
    
    # Test 2: Vyhledávání
    print("\n🔍 TEST 2: Vyhledávání 'machine learning'")
    print("-" * 60)
    results = tools.search_reddit("machine learning", limit=3)
    
    if isinstance(results, list):
        for i, post in enumerate(results, 1):
            print(f"{i}. {post['title'][:60]}...")
            print(f"   Subreddit: r/{post['subreddit']}")
    
    # Test 3: Info o subredditu
    print("\n📊 TEST 3: Informace o r/python")
    print("-" * 60)
    info = tools.get_subreddit_info("python")
    
    if "error" not in info:
        print(f"Název: {info['title']}")
        print(f"Členů: {info['subscribers']:,}")
        print(f"Popis: {info['description'][:100]}...")
    
    # Test 4: Analýza sentimentu
    print("\n📈 TEST 4: Analýza sentimentu r/python")
    print("-" * 60)
    posts = tools.get_subreddit_posts("python", limit=20)
    sentiment = tools.analyze_sentiment(posts)
    
    if "error" not in sentiment:
        print(f"Analyzováno příspěvků: {sentiment['total_posts']}")
        print(f"Průměrné skóre: {sentiment['average_score']:.1f}")
        print(f"Průměrný upvote ratio: {sentiment['average_upvote_ratio']:.2%}")
        print(f"\nSentiment distribuce:")
        print(f"  😊 Pozitivní: {sentiment['sentiment_percentages']['positive']:.1f}%")
        print(f"  😐 Neutrální: {sentiment['sentiment_percentages']['neutral']:.1f}%")
        print(f"  😞 Negativní: {sentiment['sentiment_percentages']['negative']:.1f}%")
    
    print("\n" + "=" * 60)
    print("✅ VŠECHNY TESTY DOKONČENY!")
    print("=" * 60)


if __name__ == "__main__":
    print("🚀 Spouštím testy...\n")
    test_reddit_functions()