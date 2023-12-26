class BankAccount:

    def __init__(self,account_number, balance, date_of_opening, customer_name):
         self.account_number=account_number
         self.balance=balance
         self.date_of_opening=date_of_opening
       
         self.customer_name=customer_name
        
    def deposil(self,add_deposil):
        self.balance= self.balance+add_deposil
        return self.balance
    
    def withdraw(self,withdraw_):
        self.balance=self.balance-withdraw_
        return(self.balance)
    def check_balance(self):
        return  self.balance
    
A1 = BankAccount(112233445566, 2000, '1-1-200', "Fatema")

print("Balance after deposil: ",A1.deposil(200))
print("Balance after withdraw: ",A1.withdraw(600))
print("Balance after deposil and withdraw: ",A1.check_balance())

        
        
        