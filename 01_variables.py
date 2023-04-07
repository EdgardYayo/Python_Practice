# Variables
# En python ahi que escribir las variables en snake case osea con "_"

my_variable = "My String Variable"
print(my_variable)

my_number = 12
print(my_number)

my_bool_variable = False
print(my_bool_variable)

# Funciones del Sistema
# La funcion print() puede recibir varios parametros
# el metodo len() devuelve el largo de una list o un str
# el metodo str() convierte un numero a un string
# el metodo int() convierte un string a un entero pero debe ser un string con caracteres numericos

print(my_variable, 'tiene un largo de:', len(my_variable), 'caracteres')
print(type(str(my_number)))

my_numy = "2"
number = int(my_numy)

print(type(my_numy))
print(my_numy)
print(type(number))
print(number)

# Se pueden escribir muchas variables en una sola linea
# OJO No Abusar de esta sintaxis

name, surname, age = "Edgard", "Pazos", 28
print(name, surname, age)


# Las variables se pueden reasignar 

address = "Mi casa"
address = "Tu casa"
address = 131

# ¿Forzamos el tipado? 🤔

beach: str = "Ensenada"
beach = "Rosarito"
beach = 90 # Realmente no lo podemos forzar

# Uso de Inputs para recoger datos

my_name = input("What's your name? ")
print(my_name)

