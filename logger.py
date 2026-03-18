import json
from datetime import datetime

def log_trade(data):
    with open("trades.json", "a") as f:
        f.write(json.dumps(data) + "\n")
