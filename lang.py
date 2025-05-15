import json

with open("lang.json", "r", encoding="utf-8") as f:
    TEXTS = json.load(f)

def get_text(key: str, lang: str) -> str:
    return TEXTS.get(lang, {}).get(key, key)