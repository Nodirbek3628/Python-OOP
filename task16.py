#  Kitoblar ro‘yxatini chiqarish va o‘qilganlarini ajratish**
#`Book` nomli class yozing.

# Atributlar:
# * `title`
# * `author`
# * `is_read` – boshlanishida False

# Metodlar:
# * `mark_as_read()` – kitobni o‘qilgan deb belgilaydi
# * `status()` – `"O‘qilgan"` yoki `"O‘qilmagan"` deb chiqaradi

# Topshiriq:
# * 5 ta `Book` obyekti yarating va ularni `books` listiga joylang.
# * 2 ta kitobni `mark_as_read()` bilan belgilang.
# * `for` loop orqali barcha kitoblarning holatini chiqarib bering (`status()` yordamida).
# * Faqat o‘qilgan kitoblarning nomlarini alohida chiqarib bering.

class Book:
    def __init__(self,title,author,is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self)->None:
        self.is_read = True

    def status(self)->None:
        if self.is_read:
            return "o'qilgan"
        else:
            return "o'qilmagan"

book01 = Book("Do'st orttirish","Deyl Karnegi")
book02 = Book("Atom odatlari","Jeyms Klir")
book03 = Book("Bahor Qaytmaydi","O'tkir Xoshimov")
book04 = Book("Supper miya","Davronbek Turdyev")
book05 = Book("Deep Work","Cal Newport")


book01.mark_as_read()
book03.mark_as_read()

books = [book01,book02,book03,book04,book05]

for book in books:
        print(f"{book.title} {book.status()}")
for book in books:
     if book.is_read:
        print(f"o'qilgan kitoblar  ro'yxati: {book.title}")

