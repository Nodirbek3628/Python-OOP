#12 – Multiple Bank Accounts**

# `BankAccount` nomli class yozing.

# Atributlar:

# * `owner`
# * `balance`

# Metodlar:

# * `deposit(amount)`
# * `withdraw(amount)`
# * `show_balance()` – hisobdagi mablag‘ni `print()` qiladi

# Topshiriq:

# * 3 ta hisob egasi (obyekt) yarating.
# * Har biriga turli summalarda `deposit()` va `withdraw()` amallarini bajaring.
# * Yakuniy balansni `show_balance()` orqali ko‘rsating.

class BankAccount:
    def __init__(self,owner:str)->None:
        self.owner: str = owner
        self.balance: float= 0.0
    
    def deposit(self,amount: float)->None:
        self.balance += amount
    
    def withdraw(self,amount:float)->None:
        if amount <= self.balance:
            self.balance -= amount

    def show_balance(self:str)->None:
        print(f"Balansingiz: {self.balance}")

bank01 = BankAccount("ali")
bank01.deposit(500)
bank01.withdraw(50)
bank01.show_balance()