# 10 – BankAccount klassi bilan ishlash**
# `BankAccount` nomli class yozing.

# **Atributlar:**
# * `owner` – hisob egasining ismi
# * `balance` – hisobdagi pul miqdori

# **Metodlar:**
# * `deposit(amount)`
#   * **Nima qiladi:** berilgan summani balansga qo‘shadi.
#   * **Return:** yangi balansni `print()` qiladi.

# * `withdraw(amount)`
#   * **Nima qiladi:** agar balans yetarli bo‘lsa, pul yechib beradi; aks holda ogohlantiradi.
#   * **Return:** yangi balans yoki xato xabarni `print()` qiladi.

# 📌 Maqsad: Obyekt holatini method orqali o‘zgartirishni o‘rganish.

class BankAccount:
    def __init__(self,owner:str)->None:
        self.owner: str = owner
        self.balance: float= 0.0
    
    def deposit(self,amount: float)->None:
        self.balance += amount
        print(self.balance)
    
    def withdraw(self,amount:float)->None:
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Xisobingizda mablag' yetarli emas ")

    

bank01 = BankAccount("ali")
bank01.deposit(10)
bank01.withdraw(5)
