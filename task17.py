# 17 – Bank hisoblari ro‘yxatidan jami balansni hisoblash**

# 🏦 `BankAccount` nomli class yozing.

# **Atributlar:**

# * `owner`
# * `balance`

# **Metod:**

# * `show_balance()` – balansni `print()` qiladi
# * `get_balance()` – balansni **qaytaradi (return)**

# Topshiriq:
# * 5 ta `BankAccount` obyektini yarating.
# * Ularni `accounts` ro‘yxatiga joylang.
# * `for` loop yordamida jami balansni hisoblang.
# * Jami balansni `print()` qiling.

class BankAccount:
    def __init__(self,owner:str,balance)->None:
        self.owner: str = owner
        self.balance = balance
    def show_balance(self):
        print(f"{self.owner}Balansingz:{self.balance}")
    
    def get_balance(self):
        return self.balance
  
bank01 = BankAccount("ali",75000)
bank02 = BankAccount("vali",56000)
bank03 = BankAccount("jon",47000)
bank04 = BankAccount("joxa",10000)
bank05 = BankAccount("guli",125000)

accounts = [bank01,bank02,bank03,bank04,bank05]

total = 0
for account in accounts:
    if account.balance:
        total += account.get_balance()

print(f"Jami balans:{total} so'm")

