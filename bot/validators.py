def validate_side(side:str):
    if side.upper() not in ["BUY","SELL"]:
        raise ValueError("Side must be BUY or SELL")
def validate_order_type(order_type: str):
    if order_type.upper() not in ["MARKET","LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
def validate_price(price,order_type:str):
    if order_type.upper() == "LIMIT" and price <= 0:
        raise ValueError("Price must be greater than 0 for LIMIT orders")