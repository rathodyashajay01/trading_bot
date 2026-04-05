# Binance Futures Testnet Trading Bot

## Setup

1. Clone repo
2. Create virtualenv
3. Install dependencies:
   pip install -r requirements.txt

4. Add .env file with API keys

## Run

### MARKET

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Features

- Market & Limit Orders
- BUY / SELL support
- CLI input validation
- Logging to file
- Error handling

## Assumptions

- Binance Futures Testnet is used
- Only USDT-M futures supported

## Requirements

- pip install -r requirements.txt

## Virtual Environment

- python -m venv venv
  venv\Scripts\activate

## Create a `.env` file with your own Binance Futures Testnet API keys:

- BINANCE_API_KEY=your_testnet_key
- BINANCE_API_SECRET=your_testnet_secret
