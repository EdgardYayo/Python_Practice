# THESE ARE VERY BASIC EXAMPLES OF USINGS OBJECTS AND CREATE THEM IN PYTHON.
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokémon Name", ["Pikachu", "Bulbasaur"])
# table.add_column("Type", ["Electric", "Grass"])
#
# table.align = "l"
# print(table)

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("Edgard", 28, "Male")
user_2 = User("Angela", 32, "Female")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

