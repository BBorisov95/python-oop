from project.food import Food
from project.drink import Drink
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, name: str):
        return self.do_product_loop(name)

    def remove(self, product_name: str):
        result_obj = self.do_product_loop(product_name)
        if result_obj:
            self.products.remove(result_obj)

    def do_product_loop(self, name):
        for product in self.products:
            if product.name == name:
                return product

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f'{product.name}: {product.quantity}\n'
        return result[:-1]
