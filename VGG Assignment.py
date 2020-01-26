
'''

Build a command-line Banking Application with the following functionalities:
Application starts with a prompt to the user with the following options: Press 1: create account Press 2: transaction

1. Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account. [Hint: Ensure that you data structure caters for each users account balance, you might want to initialize this to 0.0]

2. Transaction: Authenticate the user by prompting for a password, if the password is correct, user is authenticated and show the following options: Press 1: check balance Press 2: deposit Press 3: withdraw Press 4: transfer if the password is incorrect, tell the user that they are not authorized and go back to the create account option

3. Check balance: query your data structure to check the balance of the authenticated user

4. Deposit: prompt the user to enter an amount, then add the amount to the users balance

5. Withdraw: prompt the user to enter an amount, if the user does not have money in their account, tell them to deposit and move to the deposit prompt. If they user has money, print out the amount withdrawn and the available balance,

6. Transfer: prompt the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, add the amount to the beneficiaries account.
'''





def balance():
    bal = 0
    return bal


balance()


def menu1():
    print('Welcome to the Pythonista Bank of Africa')
    print('Press 1 to create an account')
    print('Press 2 for transactions')
    print('Use any other number to exit')
    selection = input()

    if selection == str(1):
        print('Enter your email: ')
        mail = input()
        print(mail)
        print('Enter your PIN')
        pin = input()
        print(pin)
        print('Hurray!!\n'
              'You have successfully created an account with Pythonista Bank of Africa!!')
        print('Your balance is: ', balance())

    else:
        if input() >= 3:
            quit()


menu1()


def menu2():
    mail = 'babyboy@gmail.com'
    password = 'hwhayd@'
    print('Input your email address')
    input(mail)
    print('Input your password')
    input(password)
    print('Press 1 to check balance')
    print('Press 2 to make a deposit')
    print('Press 3 to withdraw')
    print('Press 4 to transfer')
    selection = input()
    if selection == str(1):
        print('Your balance is ', balance())
        return menu2()
    elif selection == str(2):
        print('Enter an amount')
        amount = input()
        newBalance = int(amount) + balance()
        print(newBalance)
        return menu2()
    elif selection == str(3):
        if balance() >= 0:
            print('Enter amount')
            withdrawAmount = input()
            print('You have withdrawn: ' + withdrawAmount)
            remainingBalance = int(withdrawAmount) - int(withdrawAmount)
            print('Your available balance is: ', remainingBalance)
            return menu2()
    elif selection == str(4):
        print('Enter the email of the recipient')
        email = input()
        print('Enter amount')
        amount = input()
        remainingBalance = int(amount) - balance()
        print(remainingBalance)


menu2()
