#  11 – Book klassi bilan ishlash**
# `Book` nomli class yozing.

# **Atributlar:**
# * `title` – kitob nomi
# * `author` – muallif
# * `is_read` – True/False (kitob o‘qilganmi)

# **Metod:**
# * `mark_as_read()`
#   * **Nima qiladi:** `is_read` ni `True` ga o‘zgartiradi
#   * **Return:** `"Kitob o‘qilgan deb belgilandi"` degan `print()` chiqaradi

# * `status()`
#   * **Nima qiladi:** o‘qilganmi yoki yo‘qmi — shuni bildiradi
#   * **Return:** `"O‘qilgan"` yoki `"O‘qilmagan"` deb `print()` qiladi

class Book:
    def __init__(self,title: str,author:str ,is_read=False) -> None:
        self.title = title
        self.author = author
        self.is_read = is_read
    
    def mark_as_read(self):
        self.is_read = False
        
    def status(self)->None:
        if self.is_read:
            print("O'qilgan")
        else:
            print("Oqilmagan")

book01 = Book("O'tgan ko'nlar","Abdulla Qodiriy")
book01.mark_as_read()
book01.status()


