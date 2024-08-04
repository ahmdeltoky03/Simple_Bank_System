from User import User
from Bank import Bank

bank = Bank()
print("Welcome to {}".format(bank.name))
flag = True
while flag:
    print("Select : ")
    print("1) To create new bank_account\n2)To open an existing account\n3)To Exit")
    choice = int(input(''))
    if choice == 1:
        print("Please Enter your Details about your Name,Age,Gender and Deposit")
        user = User(input('Please Enter your account_name : '), int(input('Please Enter your Deposit : ')))
        bank.update_database(user)
        print('Account has been created Successfully and Account Number = {}'.format(user.account['account_number']))
        bank.update_database(user)


    elif choice == 2:
        print("To Ensure That You have account Entered Name and Account_Number : ")
        name = input('Enter your name : ')
        account_number = int(input('Enter your account_number : '))
        current_user = bank.authentication(name, account_number)
        if current_user:
            print(f'welcome {name}')
            # print(f'welcome {current_user.account['name']}')
            acc_open = True
            while acc_open:
                _choice = int(input("Select : \n1)Withdraw\n2)Deposit\n3)Balance\n4)Exit\n"))
                if _choice == 1:
                    current_user.withdraw(int(input('')))
                elif _choice == 2:
                    current_user.deposit(int(input('')))
                elif _choice == 3:
                    current_user.display_balance()
                else:
                    print("Thank You")
                    acc_open = False
        else:
            print('Authentication Failed!')
            print('There is no Account with This Details')


    elif choice == 3:
        print('Thank you for Dealing with us\nBank Misr')
        flag = False
