import uuid
from decimal import Decimal
from datetime import datetime

class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.account_id = uuid.uuid4()
        self.balance = Decimal(initial_balance)
        self.transactions = []

    def deposit(self, amount):
        # Додаємо кошти на рахунок
        self.balance += Decimal(amount)
        # Записуємо транзакцію
        self.transactions.append((Decimal(amount), 'депозит', datetime.now()))

    def withdraw(self, amount):
        # Перевіряємо, чи є достатньо коштів для виведення
        if self.balance >= Decimal(amount):
            # Зменшуємо баланс на виведену суму
            self.balance -= Decimal(amount)
            # Записуємо транзакцію
            self.transactions.append((Decimal(amount), 'виведення', datetime.now()))
        else:
            print("Недостатньо коштів на рахунку.")

    def get_balance(self):
        return self.balance

    def add_interest(self, rate=0.01):
        # Додаємо відсотки до балансу
        interest = self.balance * Decimal(rate)
        self.balance += interest
        # Записуємо транзакцію
        self.transactions.append((interest, 'відсотки', datetime.now()))

# Приклад використання класу
account1 = BankAccount("Основний рахунок", 1000)
print("Початковий баланс:", account1.get_balance())  # Виведе: 1000

account1.deposit(500)
print("Баланс після депозиту:", account1.get_balance())  # Виведе: 1500

account1.withdraw(200)
print("Баланс після виведення:", account1.get_balance())  # Виведе: 1300

account1.add_interest()
print("Баланс з врахуванням відсотків:", account1.get_balance())  # Виведе баланс з відсотками
