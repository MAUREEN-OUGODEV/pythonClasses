class Account:
    def __init__(self,acccountName,accountNumber,amount):
        self.accountName=acccountName
        self.accountNumber= accountNumber
        self.amount =amount

    def current_details(self) :
        return f"your accountName:{self.accountName} accountNumber: {self.accountNumber} and Balance: {self.amount}"
            
    def deposit_amount(self):
       deposit_amount=2000
       return f"Your new Balance is{self.amount +deposit_amount}"
    
    def withdraw(self):
        withdraw=1200
        return f"you have withdrawn{withdraw} , your balance is {self.amount - withdraw}"

