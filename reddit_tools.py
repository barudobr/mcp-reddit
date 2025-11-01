

import praw
from typing import List, Dict, Optional
from datetime import datetime
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT


class RedditTools:
    """Třída s nástroji pro práci s Redditem"""
    
    def __init__(self):
        """Inicializace Reddit připojení"""
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
    
    def get_subreddit_posts(
        self, 
        subreddit_name: str, 
        limit: int = 10,
        sort_by: str = "hot"
    ) -> List[Dict]:
        """
        Získá příspěvky ze subredditu
        
        Args:
            subreddit_name: Název subredditu (např. "python")
            limit: Počet příspěvků k získání (default: 10)
            sort_by: Způsob řazení - "hot", "new", "top", "rising" (default: "hot")
        
        Returns:
            List[Dict]: Seznam příspěvků s jejich detaily
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            # Výběr způsobu řazení
            if sort_by == "hot":
                posts = subreddit.hot(limit=limit)
            elif sort_by == "new":
                posts = subreddit.new(limit=limit)
            elif sort_by == "top":
                posts = subreddit.top(limit=limit)
            elif sort_by == "rising":
                posts = subreddit.rising(limit=limit)
            else:
                posts = subreddit.hot(limit=limit)
            
            # Zpracování příspěvků
            result = []
            for post in posts:
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "author": str(post.author) if post.author else "[deleted]",
                    "score": post.score,
                    "upvote_ratio": post.upvote_ratio,
                    "num_comments": post.num_comments,
                    "created_utc": datetime.fromtimestamp(post.created_utc).isoformat(),
                    "url": post.url,
                    "permalink": f"https://reddit.com{post.permalink}",
                    "selftext": post.selftext[:500] if post.selftext else "",  # První 500 znaků
                    "is_video": post.is_video,
                    "over_18": post.over_18,
                    "spoiler": post.spoiler,
                    "subreddit": subreddit_name
                }
                result.append(post_data)
            
            return result
            
        except Exception as e:
            return {"error": f"Chyba při získávání příspěvků: {str(e)}"}
    
    def search_reddit(
        self,
        query: str,
        subreddit_name: Optional[str] = None,
        limit: int = 10,
        sort_by: str = "relevance"
    ) -> List[Dict]:
        """
        Vyhledá na Redditu
        
        Args:
            query: Vyhledávací dotaz
            subreddit_name: Název subredditu (None = hledat všude)
            limit: Počet výsledků (default: 10)
            sort_by: Řazení - "relevance", "hot", "top", "new", "comments" (default: "relevance")
        
        Returns:
            List[Dict]: Seznam nalezených příspěvků
        """
        try:
            if subreddit_name:
                # Hledání v konkrétním subredditu
                subreddit = self.reddit.subreddit(subreddit_name)
                search_results = subreddit.search(query, limit=limit, sort=sort_by)
            else:
                # Hledání na celém Redditu
                search_results = self.reddit.subreddit("all").search(query, limit=limit, sort=sort_by)
            
            # Zpracování výsledků
            result = []
            for post in search_results:
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "author": str(post.author) if post.author else "[deleted]",
                    "score": post.score,
                    "num_comments": post.num_comments,
                    "subreddit": str(post.subreddit),
                    "created_utc": datetime.fromtimestamp(post.created_utc).isoformat(),
                    "permalink": f"https://reddit.com{post.permalink}",
                    "selftext": post.selftext[:300] if post.selftext else ""
                }
                result.append(post_data)
            
            return result
            
        except Exception as e:
            return {"error": f"Chyba při vyhledávání: {str(e)}"}
    
    def get_post_comments(
        self,
        post_id: str,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """
        Získá komentáře k příspěvku
        
        Args:
            post_id: ID příspěvku
            limit: Maximální počet komentářů (None = všechny)
        
        Returns:
            List[Dict]: Seznam komentářů
        """
        try:
            submission = self.reddit.submission(id=post_id)
            
            # Načtení všech komentářů
            submission.comments.replace_more(limit=0)  
            
            result = []
            comment_count = 0
            
            for comment in submission.comments.list():
                if limit and comment_count >= limit:
                    break
                
                comment_data = {
                    "id": comment.id,
                    "author": str(comment.author) if comment.author else "[deleted]",
                    "body": comment.body,
                    "score": comment.score,
                    "created_utc": datetime.fromtimestamp(comment.created_utc).isoformat(),
                    "is_submitter": comment.is_submitter,
                    "parent_id": comment.parent_id,
                    "permalink": f"https://reddit.com{comment.permalink}"
                }
                result.append(comment_data)
                comment_count += 1
            
            return result
            
        except Exception as e:
            return {"error": f"Chyba při získávání komentářů: {str(e)}"}
    
    def get_subreddit_info(self, subreddit_name: str) -> Dict:
        """
        Získá informace o subredditu
        
        Args:
            subreddit_name: Název subredditu
        
        Returns:
            Dict: Informace o subredditu
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            info = {
                "name": subreddit.display_name,
                "title": subreddit.title,
                "description": subreddit.public_description,
                "subscribers": subreddit.subscribers,
                "created_utc": datetime.fromtimestamp(subreddit.created_utc).isoformat(),
                "over18": subreddit.over18,
                "url": f"https://reddit.com/r/{subreddit.display_name}",
                "active_users": subreddit.active_user_count if hasattr(subreddit, 'active_user_count') else None
            }
            
            return info
            
        except Exception as e:
            return {"error": f"Chyba při získávání info o subredditu: {str(e)}"}
    
    def get_user_info(self, username: str) -> Dict:
        """
        Získá informace o uživateli
        
        Args:
            username: Uživatelské jméno
        
        Returns:
            Dict: Informace o uživateli
        """
        try:
            user = self.reddit.redditor(username)
            
            info = {
                "name": user.name,
                "created_utc": datetime.fromtimestamp(user.created_utc).isoformat(),
                "link_karma": user.link_karma,
                "comment_karma": user.comment_karma,
                "is_gold": user.is_gold,
                "is_mod": user.is_mod,
                "has_verified_email": user.has_verified_email if hasattr(user, 'has_verified_email') else None
            }
            
            return info
            
        except Exception as e:
            return {"error": f"Chyba při získávání info o uživateli: {str(e)}"}
    
    def analyze_sentiment(self, posts: List[Dict]) -> Dict:
        """
        Jednoduchá analýza sentimentu příspěvků
        Analyzuje pozitivitu/negativitu na základě score a upvote ratio
        
        Args:
            posts: Seznam příspěvků k analýze
        
        Returns:
            Dict: Statistiky sentimentu
        """
        if not posts or "error" in posts:
            return {"error": "Žádná data k analýze"}
        
        total_posts = len(posts)
        total_score = sum(p.get("score", 0) for p in posts)
        total_comments = sum(p.get("num_comments", 0) for p in posts)
        avg_upvote_ratio = sum(p.get("upvote_ratio", 0) for p in posts) / total_posts if total_posts > 0 else 0
        
        # Klasifikace sentimentu na základě upvote ratio
        positive = sum(1 for p in posts if p.get("upvote_ratio", 0) > 0.7)
        neutral = sum(1 for p in posts if 0.4 <= p.get("upvote_ratio", 0) <= 0.7)
        negative = sum(1 for p in posts if p.get("upvote_ratio", 0) < 0.4)
        
        return {
            "total_posts": total_posts,
            "total_score": total_score,
            "average_score": total_score / total_posts if total_posts > 0 else 0,
            "total_comments": total_comments,
            "average_comments": total_comments / total_posts if total_posts > 0 else 0,
            "average_upvote_ratio": avg_upvote_ratio,
            "sentiment_distribution": {
                "positive": positive,
                "neutral": neutral,
                "negative": negative
            },
            "sentiment_percentages": {
                "positive": (positive / total_posts * 100) if total_posts > 0 else 0,
                "neutral": (neutral / total_posts * 100) if total_posts > 0 else 0,
                "negative": (negative / total_posts * 100) if total_posts > 0 else 0
            }
        }


if __name__ == "__main__":
    print("🔧 Inicializuji Reddit Tools...")
    tools = RedditTools()
    
    print("\n📝 Test: Získávání příspěvků z r/python")
    posts = tools.get_subreddit_posts("python", limit=5)
    if posts and "error" not in posts:
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title'][:60]}...")
            print(f"   👍 {post['score']} | 💬 {post['num_comments']} komentářů")
    
    print("\n📊 Test: Analýza sentimentu")
    sentiment = tools.analyze_sentiment(posts)
    print(f"Průměrné skóre: {sentiment['average_score']:.1f}")
    print(f"Pozitivní: {sentiment['sentiment_percentages']['positive']:.1f}%")
    
    print("\n✅ Reddit Tools fungují!")
