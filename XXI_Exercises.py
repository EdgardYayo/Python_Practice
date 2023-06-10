# # Exercises 2 ✔
import random 

# for i in range(3):
#     print(random.randint(10, 25))


# members = ['John', 'Mary', 'Bob', 'Mosh', 'Rita']
# leader = random.choice(members)
# print(leader)


class Dice:
    def roll(self):
       first = random.randint(1, 6)
       second = random.randint(1, 6)
       return first, second



dado = Dice()
roll1 = dado.roll()
roll2 = dado.roll()
roll3 = dado.roll()

print(roll1, roll2, roll3)
