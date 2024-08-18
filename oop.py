# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

first_cat = Cat(cat_name="Garfield", cat_age=2)
second_cat = Cat(cat_name="meow", cat_age=3)
third_cat = Cat(cat_name="Fuzz Aldrin", cat_age=4)

def find_oldest_cat(cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

cats = [first_cat, second_cat, third_cat]

oldest_cat = find_oldest_cat(cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Exercise 2 : Dogs
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high ")

davids_dog = Dog(dog_name="Rex", dog_height=50)
print(f"david dog called {davids_dog.name} and he is {davids_dog.height} cm high ")

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog(dog_name="Teacup", dog_height=20)
print(f"sarahs dog called {sarahs_dog.name} and he is {sarahs_dog.height} cm high ")

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog!")
else:
    print(f"{sarahs_dog.name} is the bigger dog")


# Exercise 3 : Who’s the song producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure",
                 "all that glitters is gold",
                 "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()