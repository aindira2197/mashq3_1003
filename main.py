class BankCard:
    bank_name = "Agrobank"

    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_card_number(number):
        if len(number) == 16:
            return True
