# 6 – Student klassi bilan ishlash**

# `Student` nomli class yozing.
# Atributlar:
# * `name` – o‘quvchining ismi
# * `age` – o‘quvchining yoshi
# * `grade` – o‘qiyotgan sinfi

# **Metod:**
# * `info()
#   * **Nima qiladi:** o‘quvchi haqida matn ko‘rinishida ma’lumotni chiqaradi.
#   * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.
#   * **Namuna chiqish:** `"Ali, 15 yoshda, 9-sinf o‘quvchisi."`

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_info(self):
        return f"{self.name},{self.age} yoshda,{self.grade}-sinf o'quvchisi"
    
studen01 = Student("Jons",17,10)
studen02 = Student("Moxi",15,8)

print(studen01.get_info())
print(studen02.get_info())


