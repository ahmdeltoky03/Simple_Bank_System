class Bank:
    name = 'Bank Misr'
    users = []  ## list of list

    def update_database(self, name):
        self.users.append(name)

    def authentication(self, name, account_number):
        for i in range(len(self.users)):
            if name in self.users[i].account.values() and account_number in self.users[i].account.values():
                print('Authentication Successfully')
                return self.users[i]
