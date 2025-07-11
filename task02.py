# 2. **Student klassini yozing**
# Student` nomli class yarating. Quyidagi atributlar bo‘lishi kerak:
# * `name` — to‘liq ismi
# * `age` — yoshi
# * `grade` — bahosi yoki o‘qish darajasi (masalan, 9-sinf)

# Talab:
# * Har bir atribut `__init__()` orqali qiymat qabul qilsin.
# * Kodni o‘zingiz xohlagan 2-3ta object bilan sinab ko‘ring (shu fayl ichida).

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"{self.name} {self.age} yosh  xozirda {self.grade}"

student01 = Student('abbos','23','10 - sinf')
student02 = Student('ali','25','11 - sinf')

print(student01.get_info())
print(student02.get_info())