# Loops ✔

# Bucles While ######################


one_condition = True
id = 1

# Esto generaria un bucle infinito por que one_condition es siempre verdad
while one_condition:
    print(id)
    id += 1
    if id == 7: # Añadiendo esta linea el bucle se detendria cuando el id valga 7
        break

# La palabra reservada "break" sirve para detener la ejecucion de los ciclos o bucles

other_condition = 20

while other_condition < 30:
    print("Sigo siendo menor que 20")
    other_condition += 1

# Bucles For ##################

my_list = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

for element in my_list:
    print(element * 2)

# Imprimiría 1, 4, 6, 8, 10, 12, 14, 16

my_tuple = (32, "Hola", True)

my_set = { "Hola", 2, 3, False }

my_dict = { "Name": "Edgard", "Edad": 5 }

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for element in my_dict:
    print(element)

# Con el bucle For podemos recorrer e imprimir todos los elementos de listas, tuplas, sets y diccionarios, ademas podemos hacer operaciones con este elementos durantes el bucle

new_list = [ 3, 4, 5, 6, 8 ]

for ele in new_list:
    if ele == 5:
        print(ele * 2)
    elif ele == 6: 
        break
    else: 
        print(ele)


# Existe otra palabra reservada "continue" que tiene el propósito de saltar a la siguiente iteración del bucle sin ejecutar el código restante dentro del bloque de bucle actual.

for ele in new_list:
    if ele == 4:
        continue
    else:
        print(ele)


