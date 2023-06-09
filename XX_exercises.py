# Exercises ✔


# 1
word = input("Introduce una palabra: ")

for i in range(10):
    print(word)


# 2
age = int(input("¿Cual es tu edad?: "))

for i in range(age):
    print("Haz cumplido " + str(i + 1) + " años")



# 3

number = int(input("Escribe un numero entero positivo: "))

for i in range(1, number + 1, 2):
    print(i, end=", ")


# 4

n = int(input("Introduce un numero entero positivo: "))

for i in range(n, -1, -1):
    print(i, end=", ")



# 5

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))

for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))


# 6 

positive_number = int(input("Introduce un numero entero: "))

for i in range(positive_number):
    for j in range(i + 1):
        print("*", end="")
    print("")



# Other solution for # 6 exercise

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))


# 7 Creacion de un Emoji Converter
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)":"😊",
        ":(":"😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))