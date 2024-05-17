from abc import abstractmethod, ABC
import os
import time


class Account(ABC):
    _transactions = []

    def __init__(self, number: int, balance: int):
        self.number = number
        self.balance = balance

    def to_account(self, amount):
        self.balance += amount
        self._transactions.append(amount)

    def from_account(self, amount):
        self.balance -= amount
        self._transactions.append(-amount)

    def show_balance(self):
        return self.balance

    @property
    def transactions(self):
        return self._transactions

    @abstractmethod
    def __str__(self):
        return f"{self.number} : {self.balance:.2f}"


class CheckingAccount(Account):

    def __init__(self, balance):
        self.b = balance
        self.min_amount = 10000

    def can_make_amount(self):
        if self.min_amount < self.b:
            return True
        else:
            raise Exception(
                "When you don't have money why do you want an account????")

    def __str__(self):
        return f"CheckingAccount, Number : {self.number}, Balance : {self.balance}"


class SavingAccount(Account):
    def __init__(self, number, balance):
        self.sum_in = 0
        self.sum_out = 0
        self.number = number
        self.balance = balance

    def sum_trans(self):
        if (len(self.transactions) > 0):
            for trans in self.transactions:
                if trans > 0:
                    self.sum_in += trans
                else:
                    self.sum_out += -trans
            return self.sum_in / self.sum_out
        else:
            print("You haven't done ant transactions")

    def __str__(self):
        return f"Saving Account, Number : {self.number} , Balance : {self.balance}"


class CurrencyAccount(Account):

    @staticmethod
    def show_balance_USA(balance):
        print("Currenct balance in USA : ", balance / 50000)

    def transactions_USA(self):
        return [trans / 50000 for trans in self.transactions]

    def __str__(self):
        return f"Balance in USA today is : {self.balance / 50000}"


class Customer:
    def __init__(self, acc_type, ssn, name):
        self.acc_type = acc_type
        self.ssn = ssn
        self.name = name

    def make_bank_account(self, number, balance):
        self.bank_account = CurrencyAccount(number, balance)

    def make_save_account(self, number, balance):
        self.save_account = SavingAccount(number, balance)

    def make_curr_account(self, number, balance):
        self.curr_account = CurrencyAccount(number, balance)

    def static_method(self, balance):
        CurrencyAccount.show_balance_USA(balance)

    def show_balance(self):
        return self.bank_account.show_balance()

    def make_deposit(self, amount):
        self.bank_account.to_account(amount)

    def make_withdraw(self, amount):
        self.bank_account.from_account(amount)

    def __gt__(self, other):
        if isinstance(other, customer or int):
            return self.balance > other.balance

    def make_transfer(self, account1, account2, amount):
        if amount > account1:
            raise Exception("Not enough balance")
        else:
            account1.make_withdraw(amount)
            account2.make_deposit(amount)
            print(
                f"Balance of 1st account: {account1.balance}, Balance of 1st account: {account2.balance}")


def main_menu():
    print("\nWhat account would you like to create ?\n1.Banking_account\n2.Saving_account\n3.Currency_account")
    c1 = int(input("\nYour choice?(1,2,3) "))
    os.system("cls")
    if c1 == 1:
        number, balance = map(int, input(
            "\nEnter your number and balance : ").split())
        check = CheckingAccount(balance)
        if check.can_make_amount():
            customer.make_bank_account(number, balance)
            print("\nAccount created")
            print("\nChoose your action :\n1.Make_deposit\n2.Make_withdraw\n3.Make_transfer\n4.Show_balance\n5.exit")
            c2 = int(input("\nYour choice?(1,2,3,4,5) "))
            os.system("cls")
            menu1(c2)
    if c1 == 2:
        number, balance = map(int, input(
            "\nEnter your number and balance : ").split())
        check = CheckingAccount(balance)
        if check.can_make_amount():
            customer.make_save_account(number, balance)
            print("\nAccount created")
            print("\nChoose your action :\n1.See in_money/out_money\n2.Info\n3.exit")
            c2 = int(input("\nYour choice?(1,2,3) "))
            os.system("cls")
            menu2(c2)
    if c1 == 3:
        number, balance = map(int, input(
            "\nEnter your number and balance : ").split())
        check = CheckingAccount(balance)
        if check.can_make_amount():
            customer.make_curr_account(number, balance)
            print("\nAccount created")
            print(
                "\nChoose your action :\n1.Balance in USA\n2.Transactions in USA\n3.Info\n4.exit ")
            c2 = int(input("\nYour choice?(1,2,3,4) "))
            os.system("cls")
            menu3(c2, balance)


def menu1(c2):
    if c2 == 1:
        amount = int(input(("Amount? ")))
        customer.make_deposit(amount)
        print(
            f"\nTransaction list : {customer.bank_account.transactions}")
        print("\nChoose your action :\n1.Make_deposit\n2.Make_withdraw\n3.Make_transfer\n4.Show_balance\n5.exit")
        c2 = int(input("\nYour choice?(1,2,3,4,5) "))
        os.system("cls")
        menu1(c2)
    elif c2 == 2:
        amount = int(input(("Amount? ")))
        customer.make_withdraw(amount)
        print(
            f"\nTransaction list : {customer.bank_account.transactions}")
        print("\nChoose your action :\n1.Make_deposit\n2.Make_withdraw\n3.Make_transfer\n4.Show_balance\n5.exit")
        c2 = int(input("\nYour choice?(1,2,3,4,5) "))
        os.system("cls")
        menu1(c2)
    elif c2 == 3:
        amount = int(input(("Amount? ")))
        number1, balance1 = map(int, input(
            "\nEnter number and balance for the from_account: ").split())
        number2, balance2 = map(int, input(
            "Enter number and balance for the from_account: ").split())
        print(f"\nNew balance of the first account: {balance1 - amount}")
        print(f"New balance of the second account : {balance2 + amount}")
        print("\nChoose your action :\n1.Make_deposit\n2.Make_withdraw\n3.Make_transfer\n4.Show_balance\n5.exit")
        c2 = int(input("\nYour choice?(1,2,3,4,5) "))
        os.system("cls")
        menu1(c2)
    elif c2 == 4:
        print(f"Current balance is : {customer.show_balance()}")
        print("\nChoose your action :\n1.Make_deposit\n2.Make_withdraw\n3.Make_transfer\n4.Show_balance\n5.exit")
        c2 = int(input("\nYour choice?(1,2,3,4,5) "))
        os.system("cls")
        menu1(c2)
    else:
        main_menu()


def menu2(c2):
    if c2 == 1:
        print(customer.save_account.sum_trans())
        print("\nChoose your action :\n1.See in_money/out_money\n2.Info\n3.exit")
        c2 = int(input("\nYour choice?(1,2,3) "))
        os.system("cls")
        menu2(c2)
    elif c2 == 2:
        print(customer.save_account)
        print("\nChoose your action :\n1.See in_money/out_money\n2.Info\n3.exit")
        c2 = int(input("\nYour choice?(1,2,3) "))
        os.system("cls")
        menu2(c2)
    else:
        main_menu()


def menu3(c2, balance):
    if c2 == 1:
        customer.static_method(balance)
        print("\nChoose your action :\n1.Balance in USA\n2.Transactions in USA\n3.Info\n4.exit ")
        c2 = int(input("\nYour choice?(1,2,3,4) "))
        os.system("cls")
        menu3(c2, balance)
    elif c2 == 2:
        os.system("cls")
        print("Transaction list in : ", customer.curr_account.transactions_USA())
        print("\nChoose your action :\n1.Balance in USA\n2.Transactions in USA\n3.Info\n4.exit ")
        c2 = int(input("\nYour choice?(1,2,3,4) "))
        os.system("cls")
        menu3(c2, balance)
    elif c2 == 3:
        print(customer.curr_account)
        print("\nChoose your action :\n1.Balance in USA\n2.Transactions in USA\n3.Info\n4.exit ")
        c2 = int(input("\nYour choice?(1,2,3,4) "))
        menu3(c2, balance)
    else:
        main_menu()


acc_type, ssn, name = input("Enter your information : ").split()
if acc_type != "B" and acc_type != "C" and acc_type != "S":
    print("\nacc_type should be S or C or B")
    acc_type = input("\nacc_type : ")
customer = Customer(acc_type, ssn, name)
print("\nYou are now a customer!!!")
main_menu()
