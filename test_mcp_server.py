

from reddit_tools import RedditTools
import json


def test_reddit_functions():
    
    
    tools = RedditTools()
    
    print("=" * 60)
    print("Reedit function test")
    print("=" * 60)
    
    
    print("\nGetting output from r/python")
    print("-" * 60)
    posts = tools.get_subreddit_posts("python", limit=3, sort_by="hot")
    
    if isinstance(posts, list):
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title'][:60]}...")
            print(f"   {post['score']} |  {post['num_comments']} comments")
  
    print("\n TEST 2: Searchíng 'machine learning'")
    print("-" * 60)
    results = tools.search_reddit("machine learning", limit=3)
    
    if isinstance(results, list):
        for i, post in enumerate(results, 1):
            print(f"{i}. {post['title'][:60]}...")
            print(f"   Subreddit: r/{post['subreddit']}")
    
    
    print("\nTEST 3: Information about r/python")
    print("-" * 60)
    info = tools.get_subreddit_info("python")
    
    if "error" not in info:
        print(f"Název: {info['title']}")
        print(f"Členů: {info['subscribers']:,}")
        print(f"Popis: {info['description'][:100]}...")
    

    print("\n📈 TEST 4: Sentiment analysis r/python")
    print("-" * 60)
    posts = tools.get_subreddit_posts("python", limit=20)
    sentiment = tools.analyze_sentiment(posts)
    
    if "error" not in sentiment:
        print(f"Number of analysed posts: {sentiment['total_posts']}")
        print(f"Average score: {sentiment['average_score']:.1f}")
        print(f"Average upvote ratio: {sentiment['average_upvote_ratio']:.2%}")
        print(f"\nSentiment distribuce:")
        print(f"  Positive: {sentiment['sentiment_percentages']['positive']:.1f}%")
        print(f"  Neutral {sentiment['sentiment_percentages']['neutral']:.1f}%")
        print(f"  Negative: {sentiment['sentiment_percentages']['negative']:.1f}%")
    
    print("\n" + "=" * 60)
    print("All tests done")
    print("=" * 60)


if __name__ == "__main__":
    print("Tests starting\n")
    test_reddit_functions()
