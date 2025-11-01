# Reddit MCP Actor

Integrace Reddit sociální platformy s Model Context Protocol (MCP) pro snadný přístup AI agentů k datům z Redditu.

## 📋 Co tento projekt dělá

Tento Actor propojuje Reddit API s MCP protokolem, což umožňuje AI aplikacím:
- 📝 Získávat příspěvky ze subredditů
- 🔍 Vyhledávat na Redditu
- 💬 Analyzovat komentáře
- 📊 Sledovat trendy a sentiment
- 👤 Získávat informace o uživatelích a komunitách

## 🚀 Rychlý start

### 1. Instalace závislostí

```bash
pip install -r requirements.txt
```

### 2. Konfigurace Reddit API

1. Přihlaste se na [Reddit](https://reddit.com)
2. Jděte na https://www.reddit.com/prefs/apps
3. Klikněte na "create application" nebo "create another app"
4. Vyplňte:
   - **name:** `reddit-mcp-actor`
   - **App type:** Zaškrtněte **"script"**
   - **redirect uri:** `http://localhost:8080`
5. Zkopírujte `client_id` a `client_secret`

### 3. Vytvoření .env souboru

```bash
# Zkopírujte šablonu
cp .env.template .env

# Vyplňte své hodnoty v .env:
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=reddit-mcp-actor/1.0
```

### 4. Test připojení

```bash
python test_reddit_connection.py
```

### 5. Test MCP serveru

```bash
python test_mcp_server.py
```

### 6. Spuštění MCP serveru

```bash
python reddit_mcp_server.py
```

## 🔧 Dostupné nástroje (MCP Tools)

### 1. `get_subreddit_posts`
Získá příspěvky ze subredditu.

**Parametry:**
- `subreddit_name` (povinný): Název subredditu
- `limit` (nepovinný): Počet příspěvků (default: 10)
- `sort_by` (nepovinný): Řazení - "hot", "new", "top", "rising"

**Příklad:**
```json
{
  "subreddit_name": "python",
  "limit": 10,
  "sort_by": "hot"
}
```

### 2. `search_reddit`
Vyhledá příspěvky na Redditu.

**Parametry:**
- `query` (povinný): Vyhledávací dotaz
- `subreddit_name` (nepovinný): Název subredditu
- `limit` (nepovinný): Počet výsledků (default: 10)
- `sort_by` (nepovinný): Řazení - "relevance", "hot", "top", "new"

**Příklad:**
```json
{
  "query": "machine learning",
  "limit": 20,
  "sort_by": "relevance"
}
```

### 3. `get_post_comments`
Získá komentáře k příspěvku.

**Parametry:**
- `post_id` (povinný): ID příspěvku
- `limit` (nepovinný): Max počet komentářů

**Příklad:**
```json
{
  "post_id": "abc123",
  "limit": 50
}
```

### 4. `get_subreddit_info`
Získá informace o subredditu.

**Parametry:**
- `subreddit_name` (povinný): Název subredditu

**Příklad:**
```json
{
  "subreddit_name": "python"
}
```

### 5. `get_user_info`
Získá informace o uživateli.

**Parametry:**
- `username` (povinný): Uživatelské jméno

**Příklad:**
```json
{
  "username": "spez"
}
```

### 6. `analyze_posts_sentiment`
Analyzuje sentiment příspěvků.

**Parametry:**
- `subreddit_name` (nepovinný): Název subredditu
- `search_query` (nepovinný): Vyhledávací dotaz
- `limit` (nepovinný): Počet příspěvků k analýze (default: 50)

**Příklad:**
```json
{
  "subreddit_name": "technology",
  "limit": 100
}
```

## 📁 Struktura projektu

```
reddit-mcp-actor/
├── reddit_mcp_server.py      # Hlavní MCP server
├── reddit_tools.py            # Funkce pro práci s Reditem
├── config.py                  # Konfigurace
├── test_reddit_connection.py # Test Reddit připojení
├── test_mcp_server.py        # Test MCP serveru
├── requirements.txt           # Python závislosti
├── .env                       # Přístupové údaje (NECOMMITOVAT!)
├── .env.template             # Šablona pro .env
├── .gitignore                # Git ignore pravidla
└── README.md                 # Tato dokumentace
```

## 🔐 Bezpečnost

- ⚠️ **NIKDY** nenahrávejte `.env` soubor na GitHub!
- `.gitignore` automaticky ignoruje `.env` soubor
- Své API klíče nikdy nesdílejte s nikým

## 🐛 Řešení problémů

### `ModuleNotFoundError: No module named 'dotenv'`
```bash
pip install -r requirements.txt
```

### `REDDIT_CLIENT_ID není nastavené`
Zkontrolujte, že máte správně vyplněný `.env` soubor.

### `401 Unauthorized`
Zkontrolujte, že máte správné `client_id` a `client_secret`.

### `403 Forbidden`
Reddit možná blokuje příliš mnoho požadavků. Počkejte chvíli a zkuste znovu.

## 📚 Použité technologie

- **Python 3.8+**
- **PRAW** - Python Reddit API Wrapper
- **MCP** - Model Context Protocol
- **python-dotenv** - Načítání .env souborů

## 🤝 Jak to používat s AI

Tento MCP server můžete použít s jakýmkoliv MCP-kompatibilním AI systémem:

1. Spusťte server: `python reddit_mcp_server.py`
2. AI systém se připojí přes MCP protokol
3. AI může volat nástroje jako `get_subreddit_posts`, `search_reddit` atd.
4. Server vrací data ve standardním MCP formátu

## 📈 Příklady použití

### Monitoring subredditu
```python
# Sledování nových příspěvků v r/python
posts = get_subreddit_posts("python", limit=50, sort_by="new")
```

### Analýza sentimentu
```python
# Analýza nálady v r/technology
sentiment = analyze_posts_sentiment(subreddit_name="technology", limit=100)
```

### Vyhledávání trendů
```python
# Hledání diskusí o AI
results = search_reddit("artificial intelligence", limit=50)
```

## 📝 Licence

Tento projekt je open source a volně použitelný pro vzdělávací a vývojové účely.

## 🙋 Podpora

Pokud narazíte na problémy, zkontrolujte:
1. Máte správně nastavený `.env` soubor?
2. Jsou nainstalované všechny závislosti?
3. Je aktivované virtuální prostředí?
4. Funguje připojení k internetu?

---

**Vytvořeno v rámci tutoriálu Reddit MCP Integration** 🚀
