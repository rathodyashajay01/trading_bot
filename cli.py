import argparse
import logging

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        client = BinanceFuturesClient()

        print("\n📌 ORDER REQUEST")
        print(vars(args))

        result = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n✅ ORDER SUCCESS")
        print(result)

    except Exception as e:
        logging.error(str(e))
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()