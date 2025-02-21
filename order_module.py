# order_module.py

from discount_module import apply_discount

def calculate_total_price(order_items):
    """
    Изчислява общата цена на поръчката, като прилага отстъпки.
    """
    total_price = sum(item['price'] * item['quantity'] for item in order_items)
    return apply_discount(total_price)