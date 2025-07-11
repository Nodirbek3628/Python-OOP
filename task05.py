# Product klassini yozing**

# 🛍️ `Product` nomli class yozing. Do‘kon mahsulotlarini ifodalasin:

# * `name` — mahsulot nomi
# * `price` — mahsulot narxi (masalan, 12999.99)
# * `category` — mahsulot turi (masalan, “electronics”)
# * `in_stock` — mahsulot omborda bormi (True/False)

class Product:
    def __init__(self,name,price,category,in_stock):
        self.name = name
        self.price = price 
        self.category = category
        self.in_stock = in_stock
        

product01 = Product("Cola",6999.99,"food",True)
product02 = Product("Tort",55000.0,"food",False)

print(product01.name,product01.price)
print(product02.name,product02.price)