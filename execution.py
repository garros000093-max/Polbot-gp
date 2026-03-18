def simulate_trade(side, price, size, fair):
    edge = fair - price

    # simulate win probability
    if edge > 0:
        pnl = size * edge
    else:
        pnl = -size * abs(edge)

    print(f"{side} | price={price:.2f} | pnl={pnl:.3f}")
    return pnl
