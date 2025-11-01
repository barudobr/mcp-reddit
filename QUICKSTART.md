Quick Installation Guide - Reddit MCP Actor
Step 1: Download Files
All files are ready for download.
Step 2: Installation
1. Create Project Directory
bashmkdir reddit-mcp-actor
cd reddit-mcp-actor
2. Copy All Files
Copy all downloaded files into this directory.
3. Create Virtual Environment
bashpython -m venv venv
4. Activate Virtual Environment
Windows:
bashvenv\Scripts\activate
Mac/Linux:
bashsource venv/bin/activate
5. Install Dependencies
bashpip install -r requirements.txt
6. Obtain Reddit API Credentials

Log in to https://reddit.com
Navigate to https://www.reddit.com/prefs/apps
Click "create application"
Fill in the form with name as reddit-mcp-actor, type as script, and redirect uri as http://localhost:8080
Copy your client_id and client_secret

7. Create Environment File
Copy .env.template and rename to .env:
Windows:
bashcopy .env.template .env
Mac/Linux:
bashcp .env.template .env
```

Edit the .env file with your credentials:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=reddit-mcp-actor/1.0
8. Test Connection
bashpython test_reddit_connection.py
Expected output will confirm successful connection and display top posts from r/python.
9. Test MCP Server
bashpython test_mcp_server.py
10. Run MCP Server
bashpython reddit_mcp_server.py
Installation Complete
Your Reddit MCP Actor is ready for use.
