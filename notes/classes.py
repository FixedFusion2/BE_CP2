# TE Classes Notes

#A Class is a blueprint for an object.
#Use keyword class

#Example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
    def __str__(self):
        return f"\nName = {self.name} \nspecies = {self.species} \nage = {self.age}\n"
dog = Animal("Knight", "dog", 8)
print(dog)

bunny = Animal("snowball", "rabbit", 2)
print(bunny)

#Cookies are objects
#Cookie cutters are classes

#Example 2

class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"
first = ClassPeriod("Computer Programming 2", room = 200)
second = ClassPeriod("Computer Programming 3", room = 200 )
third  = ClassPeriod("Computer Science Principles", room = 200)

print(first,second,third)