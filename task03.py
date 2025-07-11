# ### ✅ 3. **User klassini yozing**

# User` klassi yarating. U foydalanuvchi haqida quyidagi atributlarni saqlasin:
# * `username` — login nomi
# * `email` — elektron pochta manzili
# * `is_active` — foydalanuvchi aktivmi (True/False)

#Talab:
# Ob’ekt yaratganda, barcha atributlar qiymatini olish kerak.
# is_active` uchun True yoki False qiymat kiritilsin.


class User:
    def __init__(self,username,email,is_active):
        self.username = username
        self.email = email
        self.is_active = is_active
    
    def get_info(self):
        status = "Aktiv" if self.is_active else "Aktiv emas"
        return f"{self.username} | {self.email} | {status}"
    

User01 = User('Alisher','alisher@gmail.com',False)
User02 = User('Jons','jons@gmail.com',True)

print(User01.get_info())
print(User02.get_info())
        