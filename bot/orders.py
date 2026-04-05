import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} qty={quantity} price={price}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.place_order(**params)

        logging.info(f"Response: {response}")

        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise