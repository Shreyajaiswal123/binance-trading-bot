from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    client = get_client()

    try:
        logger.info(f"Placing {order_type} order: {symbol} {side} {quantity}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise