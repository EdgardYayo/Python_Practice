# Dictionaries ✔

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "id": 1,
    "name": "edgard",
    "lastname": "pazos",
    "languages": ["JavaScript", "Python"]
}

# Se puede acceder a los valores de las claves de los diccionarios
# asi nombredeldiccionario[clave] y esto nos daria el valor
print(my_other_dict)
print(my_other_dict["id"])
print(my_other_dict["name"])
print(my_other_dict["languages"][0])

print(len(my_other_dict))


# Asi como tambien cambiar los valores de las claves
my_other_dict["lastname"] = "Inda"
print(my_other_dict)

# Para borrar una clave-valor de un diccionario con la palabra clave "del"
del my_other_dict["id"]
print(my_other_dict)

# Para comprobar si una clave existe en el diccionario con la palabra clave "in"
print("Edgard" in my_other_dict) # False
print("name" in my_other_dict) # True

# Para obtener todos los elementos clave-valor de un diccionario con el metodo items()
print(my_other_dict.items())


# Para obtener las claves de un diccionarios con el metodo keys() y los valores con el metodo values()
print(my_other_dict.keys()) 
print(my_other_dict.values()) 

# Para crear un diccionario con claves con valores none con el metodo "fromkeys()"
my_new_dict = dict.fromkeys(("Nombre", "Apellido"))
print(my_new_dict)