"""
Don't generate lab for this module
"""
class InsufficientFundError(Exception):
    pass

class BankAccount:
    acc_counter = 100

    def __init__(self, name, balance):
        self.name = name
        self.__acc = BankAccount.acc_counter
        self.__balance = balance
        BankAccount.acc_counter += 1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if(balance > 0):
            self.__balance = balance
        else:
            self.__balance = 0

    def func_withdraw(self, amount):
        if self.__balance > amount and amount > 0:
            self.__balance -= amount
        else:
            raise InsufficientFundError("insufficient Fund")

    def get_balance(self):
        return self.balance

    def fun_get_details(self):
        return (f'account Number: {self.__acc}, name: {self.name}, balance : {self.__balance}')

james = BankAccount('James', 1000)
ashok = BankAccount('ashok', 500)
print(james.fun_get_details())
print(ashok.fun_get_details())
james.__acc = 500
print(james.fun_get_details())
print(james.__acc)
print(dir(james))