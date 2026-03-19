# Binance Trading Bot (Testnet)

## Features
- Market Order
- Limit Order
- Stop-Limit Order
- CLI using Typer
- Logging and Error Handling

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. Create .env file:
   API_KEY=your_key
   API_SECRET=your_secret

## Run

### Market Order
python cli.py trade --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

### Limit Order
python cli.py trade --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 60000

### Stop-Limit Order
python cli.py trade --symbol BTCUSDT --side BUY --order-type STOP_LIMIT --quantity 0.001 --price 61000 --stop-price 60500