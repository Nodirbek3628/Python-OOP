#  9 – User klassi bilan ishlash**
# `User` nomli class yozing.

# **Atributlar:**
# * `username` – login nomi
# * `email` – foydalanuvchi emaili
# * `is_active` – foydalanuvchi aktivmi (True/False)

# **Metodlar:**
# * `activate()`
#   * **Nima qiladi:** `is_active` ni `True` ga o‘zgartiradi va foydalanuvchi faollashtirilgani haqida xabar beradi.
#   * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.

# * `deactivate()`
#   * **Nima qiladi:** `is_active` ni `False` ga o‘zgartiradi va foydalanuvchi bloklangani haqida xabar beradi.
#   * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.

class User:
    def __init__(self,username,email,is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        if self.is_active:
            return f"{self.username} Foydalanuvchi faollashtirildi"
        
    def deactivate(self):
        if self.is_active == False:
            return f"{self.username} Foydalanuvchi bloklandi "

user01 = User("alisher","alisher@gmail.com",True)
user02 = User("Valijon","valijon@gmail.com",False)

print(user01.activate())
print(user02.deactivate())

