import feedparser
from trigger_keywords import TRIGGERS

FEEDS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed",
    "https://cryptoslate.com/feed/",
    "https://www.newsbtc.com/feed/",
    "https://bitcoinmagazine.com/.rss/full",
    "https://www.theblock.co/feeds/rss",
    "https://cryptopotato.com/feed/"
]

def get_triggers():
    results = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:10]:
            title = entry.title.lower()
            summary = entry.get("summary", "").lower()
            url = entry.link

            for keyword in TRIGGERS["bullish"]:
                if keyword.lower() in title or keyword.lower() in summary:
                    results.append(f"🚀 Bullish news: {entry.title}\n{url}")
                    break

            for keyword in TRIGGERS["bearish"]:
                if keyword.lower() in title or keyword.lower() in summary:
                    results.append(f"📉 Bearish news: {entry.title}\n{url}")
                    break
    return results
