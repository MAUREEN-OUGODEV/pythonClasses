class Account:
    def __init__(self,accountName,accountNumber,amount):
        self.accountName=accountName
        self.accountNumber= accountNumber
        self.amount =amount

    def current_details(self) :
        return f"your accountName:{self.accountName} accountNumber: {self.accountNumber} and Balance: {self.amount}"
            
    def deposit_amount(self,deposit):
       self.amount +=deposit
      
       return f"Your new Balance is{self.amount}"
    
    def withdraw(self,withdraw):
       
        return f"you have withdrawn{withdraw} , your balance is {self.amount - withdraw}"

