import requests

def get_binance_price():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=2)
        return float(r.json()["price"])
    except:
        return None

def get_polymarket(slug):
    try:
        r = requests.get(f"https://gamma-api.polymarket.com/markets?slug={slug}", timeout=3)
        return r.json()[0]
    except:
        return None

def extract_prices(market):
    yes = no = 0.5
    for t in market["tokens"]:
        if t["outcome"].lower() in ["yes","up"]:
            yes = float(t["price"])
        if t["outcome"].lower() in ["no","down"]:
            no = float(t["price"])
    return yes, no
