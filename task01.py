# Car` nomli class yozing. Quyidagi atributlarni o‘z ichiga olishi kerak:
# * `brand` — mashina brendi (masalan, “BMW”)
# * `model` — model nomi (masalan, “X5”)
# * `year` — ishlab chiqarilgan yili (masalan, 2022)

# 📝 **Talab:
# * `__init__()` konstruktor orqali atributlarni qabul qilsin.
# * Hech qanday metod yozilmaydi, faqat class va atributlar.

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

car01 = Car('chevrolet','nexia 2','2007')
car02 = Car('chevrolet','nexia 3','2020')
car01 = Car('chevrolet','lasetti','2018')

print('chevrolet','nexia 2 ', '2007')
print('chevrolet','nexia 3 ', '2020')
print('chevrolet','lasetti ', '2018')

