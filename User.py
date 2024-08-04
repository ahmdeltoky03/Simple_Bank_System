from random import randint


class User:
    # _balance = 0

    ## {name : name ,holding : balance}
    account = {}

    def __init__(self, name, _balance):
        self.account['name'] = name
        self.account['holding'] = _balance
        self.account['account_number'] = randint(1, 100)

    def deposit(self, amount):
        # self._balance += amount
        self.account['holding'] += amount
        print('Operation Done Successfully\n')
        print('Amount that has been deposited {} '.format(amount))
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.account['holding']:
            print('Insufficient Operation , Balance is not enough , balance = {}'.format(self.account['holding']))
        else:
            # self._balance -= amount
            self.account['holding'] -= amount
            print('Operation Done Successfully')
            print('Amount That Has Been Withdrawn = {} '.format(amount))
            self.display_balance()

    def display_balance(self):
        print('Balance Now = {}'.format(self.account['holding']))


user_1 = User('ahmed', 2000)
# user_1.display_balance()
user_1.withdraw(2000)
