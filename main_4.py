class BankAccount:
    # Статическое поле класса для отслеживания количества открытых счетов
    num_accounts = 0

    def __init__(self, account_holder, balance=0):
        # Поля экземпляра класса
        self.account_holder = account_holder
        self.balance = balance

        # Увеличиваем количество открытых счетов при создании нового экземпляра
        BankAccount.num_accounts += 1

    def deposit(self, amount):
        """Метод экземпляра для внесения средств на счет."""
        self.balance += amount
        print(f"Deposit: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Метод экземпляра для снятия средств со счета."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal: ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        """Метод экземпляра для получения текущего баланса."""
        return self.balance

    @staticmethod
    def calculate_interest(balance, interest_rate=0.03):
        """Статический метод для расчета процентов на счете."""
        return balance * interest_rate

    @classmethod
    def get_num_accounts(cls):
        """Метод класса для получения общего количества открытых счетов."""
        return cls.num_accounts

# Пример использования класса BankAccount
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.deposit(200)
account1.withdraw(50)

interest_amount = BankAccount.calculate_interest(account1.get_balance())
print(f"Interest earned on account1: ${interest_amount}")

total_accounts = BankAccount.get_num_accounts()
print(f"Total number of accounts: {total_accounts}")
