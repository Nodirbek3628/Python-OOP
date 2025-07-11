# 7 – Movie klassi bilan ishlash**
# `Movie` nomli class yozing.
# **Atributlar:**
# * `title` – film nomi
# * `genre` – janri
# * `duration` – davomiyligi (daqiqa)
# * `rating` – film bahosi (float, masalan, 8.5)
# **Metod:**
# * `show_summary()`
#   * **Nima qiladi:** film nomi, janri va bahosini bir qatorda chiqaradi.
#   * **Return:** hech nima qaytarmaydi, `print()` qiladi.
#   * **Namuna chiqish:** `"Inception — fantastika janridagi film. Reyting: 8.8/10."`

class Movie:
    def __init__(self,title,genre,duration,rating):
            self.title = title
            self.genre = genre
            self.duration = duration
            self.rating = rating
    def show_summary(self):
          return f"{self.title} - {self.genre} janridagi film. Reyting:{self.rating}"
    
movie01 = Movie("Aloqa","Jangari",107,7.4)
movie02 = Movie("Chempion","jangari/comedya",102,8.8)

print(movie01.show_summary())
print(movie02.show_summary())
        
