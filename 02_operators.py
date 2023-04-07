# Operadores Aritmeticos ✔

print(3 + 4) # Adicion
print(3 - 4) # Substraccion

print(3 * 4) # Multiplicacion
print(10 % 2) # Modulo (muestra el residuo de una division por ejemplo 10 % 3 ---> 1)

print(3 / 4) # Division
print(10 // 5) # Flor division, divide y redondea el resultado a un entero mas cercano hacia abajo

print(2 ** 3) # Elevar a un exponente, el de el ejemplo es 2 elevado ala 3


# Se pueden concatenar strings con el operador "+"

print("Hola" + "Python" + "¿Que tal?")
print("Hola Python" + str(3))

# Se puede multiplicar un str por un entero para imprimir varias veces
print("Hola" * 3)
print("tararara" * 5)


# Operadores Comparativos ✔ retornan un boolean True o False

print(3 > 4) # Mayor que
print(3 < 4) # Menor que

print(3 >= 4) # Mayor o igual que
print(3 <= 4) # Menor o igual que

print(3 == 4) # Igual que
print(3 != 4) # Diferente de 


# Tambien se pueden usar con otros tipos como strings, booleans y otros
# OJO pero trabaja de diferentes maneras segun el tipo

print("Hola" > "Python")
print("hola" == "Hola") 
print("Hola" != "Adios")


# Operadores Logicos ✔ and, or y not

print(True and False) # Requiere que ambas sean True o si no sera False
print(False or True) # Requiere que cualquiera sea True
print(not False) # Convierte el valor en lo contrario
print(not True)