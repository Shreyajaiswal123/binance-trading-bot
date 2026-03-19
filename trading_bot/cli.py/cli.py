import typer
from bot.orders import place_order
from bot.validators import validate_order

app = typer.Typer()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
    stop_price: float = None
):
    """
    Place a trade on Binance Futures Testnet
    """

    try:
        validate_order(symbol, side, order_type, quantity, price, stop_price)

        typer.echo("\n📌 Order Summary:")
        typer.echo(f"Symbol: {symbol}")
        typer.echo(f"Side: {side}")
        typer.echo(f"Type: {order_type}")
        typer.echo(f"Quantity: {quantity}")
        typer.echo(f"Price: {price}")
        typer.echo(f"Stop Price: {stop_price}")

        order = place_order(symbol, side, order_type, quantity, price, stop_price)

        typer.echo("\n✅ Order Placed Successfully!")
        typer.echo(f"Order ID: {order.get('orderId')}")
        typer.echo(f"Status: {order.get('status')}")
        typer.echo(f"Executed Qty: {order.get('executedQty')}")

    except Exception as e:
        typer.echo(f"\n❌ Error: {str(e)}", err=True)

if __name__ == "__main__":
    app()