import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def fair_price(open_price, current_price, elapsed):
    pct = (current_price - open_price) / open_price
    time_factor = min(elapsed / 300, 1)

    x = pct * 40
    prob = sigmoid(x)

    prob = 0.5 + (prob - 0.5) * (0.6 + time_factor / 2)

    return prob, 1 - prob

def strong_momentum(ticks):
    if len(ticks) < 6:
        return False
    return ticks[-1] > ticks[-6]
