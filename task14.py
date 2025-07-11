# 14 – Student ro‘yxatidan eng kattasini topish**
# `Student` nomli class yozing.

# Atributlar:
#`name`
#`age`

# Metod:
# * `show_info()` – ismi va yoshini chiqaradi

# Topshiriq:
# * 5 ta `Student` obyektini yarating (turli yoshda)
# * Eng katta yoshdagi talabani aniqlang (Python `max()` yoki oddiy if bilan)
# * `show_info()` metodini chaqirib natijani ko‘rsating.

class Student:
    def __init__(self,name: str ,age: int)-> None:
        self.name = name
        self.age = age

    def show_info(self)->None:
        return f"{self.name} {self.age}"
    
student01 = Student("ali",25)
student02 = Student("vali",20)
student03 = Student("moxi",22)
student04 = Student("jonni",30)
student05 = Student("bob",19)

student =[student01,student02,student03,student04,student05]

mx = max(student,key=lambda s:s.age)
print(mx.show_info())