from typing import List
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product or None:
        product = next(filter(lambda p: p.name == product_name, self.products), None)
        return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        products_info = "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
        return products_info
