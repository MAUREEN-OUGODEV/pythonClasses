
class BankAccount:
    #     Add attributes deposits and withdrawals in the init
#  method which are empty lists by default and another attribute 
# loan_balance which is zero by default.

    def __init__(self,account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.deposits = []
        self.withdrawals =[]
        self.loan_balance=0
 # Update the deposit method to append each withdrawal transaction 
# to the deposits list.
#  Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def deposit(self, amount):
        self.balance += amount  
        deposit_amount = {"amount":amount,"narration":"deposit"}
        return deposit_amount

# Update the withdrawal method to append 
# each withdrawal transaction to the withdrawals list. 
# Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            transaction = {"amount":amount, "narration":"withdrawal"}
            return self.withdrawals.append(transaction)

# Add a method check_balance which returns the account’s balance

    def check_balance(self):
        return self.balance
   

    def get_account_number(self):
        return (f'{self.account_number},{self.account_number} has {self.balance}')

    
# Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
def print_statement(self):
    transactions=self.deposits+self.withdrawals
    for transaction in transactions:
        print(transaction["narration"], "-", transaction["amount"])
    

# Add a borrow_loan method which allows a customer to borrow 
# if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their
#  total sum of all deposits.
def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "You have an outstanding loan"
        elif amount <= 100:
            return "Loan amount must be greater than 100"
        elif len(self.deposits) < 10:
            return "You must have made at least 10 deposits"
        else:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount > total_deposits / 3:
                return "Loan amount exceeds 1/3 of total deposits"
            else:
                self.loan_balance += amount
                self.balance += amount
                return "Loan of {} has been approved".format(amount)

    
