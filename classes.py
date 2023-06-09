# Classes ✔


# Example
class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

# Creamos una nueva instancia de la clase Point y la guardamos en la variable point1
point1 = Point()

# Ahora point1 tienen accesso a todos los metodos de la clase Point
point1.draw()
point1.move()


# Constructors
class Point:
    # Creamos un constructor dentro de la clase
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")



# Exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking")


pedro = Person("Pedro")
pedro.talk()


# Inheritance
# Creamos una clase general llamada Mammals
class Mammal:
     def walk(self):
        print("walk")

# Esta clase y todos sus metodos son heredados por la clase Dog y Cat
class Dog(Mammal):
    def bark(self):
        print("bark")
   

class Cat(Mammal):
    def meow(self):
        print("meow")


# Creamos una nueva instancia de la clase "Cat"
garfield = Cat()

# Y esta tiene accesso a tanto a los metodos de la clase "Cat" como alos de la clase "Mammals" por que los heredo
garfield.walk()
garfield.meow()
