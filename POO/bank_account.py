class Bank:
    def __init__(self, owner: str, current_balance = 0):
        self.owner = owner
        self.current_balance = current_balance

    def __str__(self):
        return f"Owner: {self.owner}\nAmount: {self.current_balance}"
    
    def action(self):
        while True:
            try:
                print("a) Add fund \nb) pick money? ")
                operation = input("Make a choice: ")
                if operation != 'a' and operation != 'b':
                    raise Exception
                else:
                    break

            except Exception:
                print("Select one of the options Please")
        
        if operation == 'a':
            amount = float(input("Amounts: "))
            self.add_funds(amount)
        elif operation == 'b':
            amount = float(input("Amount: "))
            self.pick_money(amount)
    

    def add_funds(self, amount):
        while True:
            try:
                if amount > 5000 or amount <=1:
                    raise Exception
                else:
                    self.current_balance += amount
                    break
            except Exception:
                print("The amount is too hight. Try with another amount")


    
    def pick_money(self, amout):
        while True:
            try:
                if self.current_balance <= 0:
                    raise Exception
                else:
                    self.current_balance -= amout
                    break
            except Exception:
                print("Saldo non sufficente")



account_1 = Bank("Rosalba Guede", 1500)
# account_1.action()    
# print(account_1.current_balance)
print(account_1)