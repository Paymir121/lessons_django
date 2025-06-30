class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance: float = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount: float):
        """пополнение счёта;"""
        print("1: пополнение:", self.__balance, "+", amount)
        self.__balance += amount
        print("1.2: пополнение:", self.__balance)

    def withdraw(self, amount: float):
        """снятие средств (не должно позволять уйти в минус);"""
        print("2: снятие:", self.__balance, "-", amount)
        if self.__balance >= amount:
            self.__balance -= amount
            print("2.2: снятие:", self.__balance)
        else:
            print("3: недостаточно средств")

    def get_balance(self):
        """получить текущий баланс."""
        print("4: текущий баланс",self.__balance)
        return self.__balance

if __name__ == '__main__':
    account = BankAccount()
    account.deposit(1000)
    account.withdraw(500)
    print(account.get_balance())
    try:
        print(account.__balance)
    except Exception as e:
        print(e)