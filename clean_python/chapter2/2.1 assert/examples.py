def apply_discount(product: dict, discount: float):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


if __name__ == "__main__":
    print(apply_discount({'name': 'apple', 'price': 10}, 0.3))
    print(apply_discount({'name': 'apple', 'price': 10}, 2))

