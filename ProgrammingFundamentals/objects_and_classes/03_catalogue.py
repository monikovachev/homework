class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        result = [i for i in self.products if i.lower().startswith(first_letter.lower())]
        return result

    def __repr__(self):
        result = f'Items in the {self.name} catalogue:\n'
        result += '\n'.join(sorted(self.products))
        return result
