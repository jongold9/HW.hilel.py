class Product:
    def __init__(self, name, product_type, price):
        if product_type not in ['coffee', 'tea', 'additional']:
            raise ValueError("Тип може бути тільки 'coffee', 'tea', або 'additional'.")
        self.name = name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f"Кава: {self.name}, ціна: {self.price}грн."


class Store:
    def __init__(self):
        self.products = []

    def import_products(self, file_name, quantity=5):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    name, product_type, price = line.strip().split(',')
                    product = Product(name, product_type, float(price))
                    self.products.extend([product] * quantity)
        except FileNotFoundError:
            print(f"Файл {file_name} не знайдено.")

    def get_products_by_type(self, product_type):
        return [product for product in self.products if product.product_type == product_type]

    def get_total_price(self):
        return sum(product.price for product in self.products)

    def sell_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return product
        print(f"Продукт {product_name} відсутній на складі.")
        return None

    def combine_products(self, product1, product2):
        if product1.product_type == 'coffee' and product2.product_type == 'additional':
            if product1.name.lower() == 'espresso':
                return Product('Latte', 'coffee', product1.price + product2.price)
        print("Неможливо поєднати ці продукти.")
        return None


# Приклад використання класів
store = Store()
store.import_products('inventory.csv')  # Припускається, що файл містить дані у форматі: name, type, price

# Виведемо всі продукти
print("Всі продукти:")
for product in store.products:
    print(product)

# Повернемо список кавових продуктів
coffee_products = store.get_products_by_type('coffee')
print("\nКавові продукти:")
for product in coffee_products:
    print(product)

# Загальна вартість продуктів
print("\nЗагальна вартість продуктів:", store.get_total_price())

# Продаж продукту
sold_product = store.sell_product('Espresso')
if sold_product:
    print("\nПроданий продукт:", sold_product)

# Поєднання продуктів
product1 = Product('Espresso', 'coffee', 27)
product2 = Product('Milk', 'additional', 5)
combined_product = store.combine_products(product1, product2)
if combined_product:
    print("\nПоєднаний продукт:", combined_product)
