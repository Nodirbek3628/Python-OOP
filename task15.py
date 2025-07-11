# 15 – Productlar narxini umumiy hisoblash**
# `Product` nomli class yozing.
# **Atributlar:**
# * `name`
# * `price`
# * `in_stock` (True/False)

# Topshiriq:
# * 5 ta mahsulot yarating.
# * Faqat `in_stock == True` bo‘lgan mahsulotlar narxini hisoblang.
# * Yakuniy natijani `print()` qiling.
#   (Masalan: `"Ombordagi mahsulotlar narxi: 274.50"`)

class Product:
    def __init__(self,name: str ,price:str,in_stock=False)->None:
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def get_info(self)->None:
        self.in_stock = True

product01 = Product("non",3000)
product02 = Product("cola",12000,True)
product03 = Product("fanta",14000)
product04 = Product("muzqaymoq",5000,True)
product05 = Product("suv",10000)

products = [product01,product02,product03,product04,product05]


total = 0 
for product in products:
    if product.in_stock:
        total +=product.price

print(f"Ombordagi maxsulotlar narxlari {total}")

