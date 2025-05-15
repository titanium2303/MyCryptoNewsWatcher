# MyCryptoNewsWatcher 🤖📈

Telegram bot that tracks important crypto news and signals possible Bitcoin price movements (rise / fall) based on key triggers.

## 🚀 Features

- Parsing news from CoinDesk and CoinTelegraph
- Detect bullish and bearish triggers
- English and Russian language support
- Telegram notifications via `/start` and `/status` commands

## 🛠 Installation

```bash
git clone https://github.com/titanium2303/MyCryptoNewsWatcher.git
cd MyCryptoNewsWatcher
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Configuration

Open ``config.py`` and insert your Telegram Bot Token:

```python
TELEGRAM_TOKEN = “your_token_here”
```

## ▶️ Run

````bash
python bot.py
```

## 📦 Deployment on VPS (optional)

Can be run as a systemd service or wrapped in Docker.

---

**Author**: titanium2303 
**License**: MIT
