# Conditionals ✔

my_condition = True

if my_condition:
    print("Verdadero")
else:
    print("Falso")

my_condition = 5 * 2

if my_condition == 11:
    print("se ejecuta la condicion de mi segundo if")


if my_condition > 10 and my_condition < 20:
    print("mayor que 10 y menor que 20")
else:
    print("es menor o igual que 10")



new_condition = 3 * 4

if new_condition == 12:
    print("Es 12")
elif new_condition > 12:
    print("Mayor que 12")
else:
    print("Es menor que 12")

print("Otra cosa")


# Tambien se pueden hacer comprobaciones con strings
my_string = "Love"

if my_string == "Lo":
    print("Es Lo")
elif my_string == "ve":
    print("Es ve")
else: 
    print("Es Love ❤")


my_string = ""

if not my_string:
    print("Mi cadena de texto esta vacia")