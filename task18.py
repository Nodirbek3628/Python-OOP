# 18 – Mahsulotlar ichidan eng qimmatini topish**
# 🛍️ `Product` nomli class yozing.

# **Atributlar:**
# * `name`
# * `price`
# * `category`

# **Metod:**
# `info()` – mahsulot nomi va narxini chiqaradi

# Topshiriq:
# * 6 ta `Product` obyektini yarating, listga joylang.
# * List ichidan eng qimmat mahsulotni toping.
# * Uning `info()` metodini chaqirib natijani ko‘rsating.

class Product:
    def __init__(self,name: str,price:float,category:str)->None:
        self.name = name
        self.price = price
        self.category = category

    def info(self)->None:
        return (f"Maxsulot nomi:{self.name}, Narxi: {self.price}")

product01 = Product("olma",5000,"meva")
product02 = Product("cola",12000,"ichimlik")
product03 = Product("fanta",13000,"ichimlik")
product04 = Product("gusht",55000,"oziq-ovqat")
product05 = Product("telefon",14000,"phone")
product06 = Product("gul",22000,"gullar")

products = [product01,product02,product03,product04,product05,product06]

mx = max(products,key=lambda pr:pr.price)

print("Eng qimmat maxulot")
print(mx.info())