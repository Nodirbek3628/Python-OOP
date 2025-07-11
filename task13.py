# 13 – Library kitoblari ro‘yxati**
# `Book` nomli class yozing.
 
# **Atributlar:**
# * `title`
# * `author`
# * `is_read` (False bo‘lib boshlansin)

# **Metodlar:**
# * `mark_as_read()`
# * `status()` – `"O‘qilgan"` yoki `"O‘qilmagan"` deb chiqaradi

#Topshiriq:
# * Kamida 4 ta `Book` obyekti yarating.
# * 2 tasini `mark_as_read()` bilan o‘qilgan deb belgilang.
# * Barcha kitoblar uchun `status()` metodini chaqiring.

class Book:
    def __init__(self,title:str,author:str,is_read = False)->None:
        self.title = title
        self.author = author
        self.is_read = is_read
    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            return "o'qilgan"
        else:
            return "o'qilmagan"

book01 = Book("Do'st orttirish","Deyl Karnegi")
book02 = Book("Atom odatlari","Jeyms Klir",True)
book03 = Book("Bahor Qaytmaydi","O'tkir Xoshimov")
book04 = Book("Supper miya","Davronbek Turdyev",True)

print(book01.status())
print(book02.status())
print(book03.status())
print(book04.status())
