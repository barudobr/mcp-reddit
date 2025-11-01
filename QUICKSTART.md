# 🚀 RYCHLÁ INSTALACE - Reddit MCP Actor

## Krok 1: Stažení souborů
✅ Všechny soubory jsou připravené ke stažení!

## Krok 2: Instalace (5 minut)

### 1. Vytvořte složku projektu
```bash
mkdir reddit-mcp-actor
cd reddit-mcp-actor
```

### 2. Zkopírujte všechny soubory do této složky

### 3. Vytvořte virtuální prostředí
```bash
python -m venv venv
```

### 4. Aktivujte virtuální prostředí

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 5. Nainstalujte závislosti
```bash
pip install -r requirements.txt
```

### 6. Získejte Reddit API přístupy

1. Přihlaste se na https://reddit.com
2. Jděte na https://www.reddit.com/prefs/apps
3. Klikněte "create application"
4. Vyplňte:
   - **name:** reddit-mcp-actor
   - **type:** script
   - **redirect uri:** http://localhost:8080
5. Zkopírujte `client_id` a `client_secret`

### 7. Vytvořte .env soubor

Zkopírujte `.env.template` a přejmenujte na `.env`:

```bash
# Windows
copy .env.template .env

# Mac/Linux
cp .env.bin/activate .env
```

Vyplňte v `.env` souboru:
```
REDDIT_CLIENT_ID=váš_client_id
REDDIT_CLIENT_SECRET=váš_client_secret
REDDIT_USER_AGENT=reddit-mcp-actor/1.0
```

### 8. Otestujte připojení
```bash
python test_reddit_connection.py
```

Měli byste vidět:
```
✅ Připojení úspěšné!
📝 Top 3 příspěvky z r/python:
...
✅ Vše funguje perfektně!
```

### 9. Otestujte MCP server
```bash
python test_mcp_server.py
```

### 10. Spusťte MCP server
```bash
python reddit_mcp_server.py
```

## 🎉 Hotovo!

Váš Reddit MCP Actor je připraven k použití!

## 📚 Co dál?

- Přečtěte si `README.md` pro detailní dokumentaci
- Prozkúmejte dostupné nástroje v MCP serveru
- Integrujte s vaší AI aplikací

## ⚠️ Časté problémy

**`ModuleNotFoundError`** → Spusťte `pip install -r requirements.txt`

**`REDDIT_CLIENT_ID není nastavené`** → Zkontrolujte `.env` soubor

**`401 Unauthorized`** → Zkontrolujte správnost `client_id` a `client_secret`

---

**Potřebujete pomoc?** Zkontrolujte sekci "Řešení problémů" v README.md
