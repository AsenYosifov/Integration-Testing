# discount_module.py

def apply_discount(total_price):
    """
    Прилага отстъпка върху общата цена според следните правила:
    - Над 1000: 10% отстъпка
    - Над 500 и до 1000: 5% отстъпка
    - 500 или по-малко: без отстъпка
    """
    if total_price > 1000:
        return total_price * 0.9
    elif total_price > 500:
        return total_price * 0.95
    else:
        return total_price