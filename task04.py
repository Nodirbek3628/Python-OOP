# 4. **Movie klassini yozing**

# `Movie` nomli class yarating. U quyidagilarni o‘z ichiga olsin:

# * `title` — kino nomi
# * `genre` — janri (masalan, “action”, “comedy”)
# * `duration` — davomiyligi (daqiqalarda)
# * `rating` — IMDB reytingi (masalan, 8.5)


class Movie:
    def __init__(self,title,genre,duration,rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def get_info(self):
        return f"*Kino nomi: {self.title} \n Janri: {self.genre} \n davomiyligi {self.duration} daqiqa  \n dunyo biyicha rating {self.rating}"
    

movie01 = Movie("So'ngi formula", "Jangari/Drama",104 , 8.5)
movie02 = Movie("Kalmar", "Hujjatli film", 35 , 3.0)

print(movie01.get_info())
print(movie02.get_info())
          
