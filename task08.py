# Product klassi bilan ishlash**

# `Product` nomli class yozing.

# **Atributlar:**

# * `name` – mahsulot nomi
# * `price` – mahsulot narxi (masalan, 199.99)
# * `category` – mahsulot turi
# * `in_stock` – boolean (True/False) — omborda bor yoki yo‘qligi

class Product:
    def __init__(self,name,price,category,in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            return f"{self.name} Omborda mavjud:"
        else:
             return f"{self.name} Hozircha tugagan"


product01 = Product("iphone 16 ",1300 ,"elsectronic",False)
product02 = Product("nexia 2 ", 56000.00, "avtomopil",True)

print(product01.check_stock())
print(product02.check_stock())


