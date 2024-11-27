class Bank_Account:
    bank_name = "Tech4GirlsBank"  # Class variable for bank name

    def _init_(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        print(f"Amount Deposited: {amount}")
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"You withdrew:{amount}")
        else:
            print("\nInsufficient balance")
            print(f"Balance: ${self.balance}")

    
account = Bank_Account()
account1 = account.deposit(4589)
 