# Reddit MCP Actor

Integration of Reddit's social media platform with Model Context Protocol for AI agent access to Reddit data.

## Overview

This Actor connects Reddit API with MCP protocol, enabling AI applications to retrieve posts from subreddits, search Reddit content, analyze comments, track trends and sentiment, and access user and community information.

## Quick Start

Install dependencies with pip install -r requirements.txt. Configure Reddit API by logging in to Reddit, navigating to https://www.reddit.com/prefs/apps, clicking create application, filling in name as reddit-mcp-actor, selecting script as app type, and using http://localhost:8080 as redirect uri. Copy your client_id and client_secret.

Create .env file fill it with your credentials: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT set to reddit-mcp-actor/1.0.

Test connection with python test_reddit_connection.py, run tests with python test_mcp_server.py, and start MCP server with python reddit_mcp_server.py.

## Available Tools

The get_subreddit_posts function retrieves posts from a subreddit with parameters subreddit_name (required), limit (optional, default 10), and sort_by (optional: hot, new, top, rising).

The search_reddit function searches Reddit for posts with parameters query (required), subreddit_name (optional), limit (optional, default 10), and sort_by (optional: relevance, hot, top, new).

The get_post_comments function retrieves comments for a post with parameters post_id (required) and limit (optional).

The get_subreddit_info function retrieves subreddit information with parameter subreddit_name (required).

The get_user_info function retrieves user information with parameter username (required).

The analyze_posts_sentiment function analyzes sentiment of posts with parameters subreddit_name (optional), search_query (optional), and limit (optional, default 50).

## Project Structure

The project includes reddit_mcp_server.py as the main MCP server, reddit_tools.py for Reddit API functions, config.py for configuration, test_reddit_connection.py for connection testing, test_mcp_server.py for server testing, requirements.txt for Python dependencies, .env for credentials (not committed), .env.template as template, .gitignore for git rules, and README.md for documentation.

## Security

Never upload .env file to GitHub. The .gitignore file automatically excludes .env file. Keep API keys confidential at all times.

## Troubleshooting

For ModuleNotFoundError run pip install -r requirements.txt. For REDDIT_CLIENT_ID not set error verify .env file is properly configured. For 401 Unauthorized check client_id and client_secret are correct. For 403 Forbidden wait as Reddit may be rate limiting requests.

## Technology Stack

Built with Python 3.8+, PRAW Python Reddit API Wrapper, MCP Model Context Protocol, and python-dotenv for environment variable management.

## Usage with AI Systems

This MCP server works with any MCP-compatible AI system. Start server with python reddit_mcp_server.py, let AI system connect via MCP protocol, allow AI to call tools like get_subreddit_posts and search_reddit, and receive data in standard MCP format.

## Example Usage

Monitor subreddit with posts equals get_subreddit_posts with parameters python, limit 50, sort_by new. Analyze sentiment with sentiment equals analyze_posts_sentiment with subreddit_name technology and limit 100. Search trends with results equals search_reddit with query artificial intelligence and limit 50.

## License

This project is open source and available for educational and development purposes.

## Support

If you encounter issues verify .env file is properly configured, all dependencies are installed, virtual environment is activated, and internet connection is working.
