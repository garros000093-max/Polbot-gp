import time
from config import *
from market import *
from strategy import *
from execution import *
from risk import RiskManager
from logger import log_trade

risk = RiskManager(INITIAL_BALANCE)

def run():
    ticks = []

    while True:
        now = int(time.time())
        ws = now - (now % 300)
        wc = ws + 300
        tl = wc - now

        price = get_binance_price()

        if price:
            ticks.append(price)

        if tl > 12:
            time.sleep(2)
            continue

        if not risk.can_trade():
            print("STOP TRADING")
            time.sleep(10)
            continue

        if len(ticks) < 6:
            continue

        open_price = ticks[0]
        current = ticks[-1]

        fair_yes, fair_no = fair_price(open_price, current, time.time() - ws)

        slug = f"btc-updown-5m-{ws}"
        market = get_polymarket(slug)

        if not market:
            continue

        yes, no = extract_prices(market)

        if not strong_momentum(ticks):
            continue

        edge_yes = fair_yes - yes
        edge_no = fair_no - no

        size = risk.position_size()

        if edge_yes > MIN_EDGE and MIN_PRICE <= yes <= MAX_PRICE:
            pnl = simulate_trade("YES", yes, size, fair_yes)
            risk.update(pnl)

            log_trade({
                "side": "YES",
                "price": yes,
                "fair": fair_yes,
                "pnl": pnl
            })

        elif edge_no > MIN_EDGE and MIN_PRICE <= no <= MAX_PRICE:
            pnl = simulate_trade("NO", no, size, fair_no)
            risk.update(pnl)

            log_trade({
                "side": "NO",
                "price": no,
                "fair": fair_no,
                "pnl": pnl
            })

        ticks = []
        time.sleep(5)

if __name__ == "__main__":
    run()
