def validate_order(symbol, side, order_type, quantity, price, stop_price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT order")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("STOP_LIMIT requires both price and stop_price")