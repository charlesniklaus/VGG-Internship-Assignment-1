from random import randint
from abc import ABCMeta, abstractmethod
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


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def transact():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def checkBalance():
        return 0

    @abstractmethod
    def transfer():
        return 0


class SavingsAccount(Account):
    # Initialize the dictionary to accept all account numbers
    def __init__(self):
        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        # Generate a random account number
        self.accountNumber = randint(10000, 99999)
        # Assign a key and values
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print('Hurray!!\n'
              'You have successfully created an account with Pythonista Bank of Africa!!. Your account number is ',
              self.accountNumber)

    def transact(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[self.accountNumber][0] == name:
                print('Authentication Successful')
                return True
            else:
                print('Authentication failed')

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print('Your deposit was successful')
        print('Available balance: ', self.checkBalance())

    def checkBalance(self):
        print('Available balance: ', self.savingsAccount[self.accountNumber][1])

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print('Insufficient balance')
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print('Withdrawal was successful')
            self.checkBalance()

    def transfer(self, transferAmount):
        print('Enter recipient email address')
        self.savingsAccount[self.accountNumber][1] -= transferAmount
        print('Transfer successful')
        self.checkBalance()


savingsAccount = SavingsAccount()
while True:
    print('Press 1 to create account')
    print('Press 2 to perform a transaction')
    print('Press 3 to exit')
    userChoice = int(input())
    if userChoice == 1:
        print('Enter your name')
        name = input()
        print('Enter your initial deposit')
        depositAmount = int(input())
        savingsAccount.createAccount(name, depositAmount)
    if userChoice == 2:
        print('Enter your name')
        name = input()
        print('Enter your account number')
        accountNumber = int(input())
        authenticationStatus = savingsAccount.transact(name, accountNumber)
        if authenticationStatus == True:
            while True:
                print('Press 1 to deposit')
                print('Press 2 to check balance')
                print('Press 3 to withdraw')
                print('Press 4 to transfer')
                print('Press 5 to enter previous menu')
                userChoice = int(input())
                if userChoice == 1:
                    print('Enter withdrawal amount to be deposited')
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 2:
                    savingsAccount.checkBalance()
                elif userChoice == 3:
                    print('Enter withdrawal amount')
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice == 4:
                    print('Enter transfer amount')
                    transferAmount = int(input())
                    savingsAccount.transfer(transferAmount)
                elif userChoice == 5:
                    break
    if userChoice == 3:
        quit()
