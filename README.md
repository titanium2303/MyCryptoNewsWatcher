# MyCryptoNewsWatcher 🤖📈

Telegram-бот, отслеживающий важные крипто-новости и сигнализирующий возможные движения цены Bitcoin (рост / падение), основываясь на ключевых триггерах.

## 🚀 Возможности

- Парсинг новостей с CoinDesk и CoinTelegraph
- Определение бычьих и медвежьих триггеров
- Поддержка английского и русского языков
- Уведомления в Telegram через команды `/start` и `/status`

## 🛠 Установка

```bash
git clone https://github.com/titanium2303/MyCryptoNewsWatcher.git
cd MyCryptoNewsWatcher
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Конфигурация

Открой `config.py` и вставь свой Telegram Bot Token:

```python
TELEGRAM_TOKEN = "your_token_here"
```

## ▶️ Запуск

```bash
python bot.py
```

## 📦 Развёртывание на VPS (опционально)

Можно запустить как systemd-сервис или обернуть в Docker. Помогу при необходимости.

---

**Автор**: titanium2303 
**Лицензия**: MIT
