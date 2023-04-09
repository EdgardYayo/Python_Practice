# Lists ✔ son como arreglos en Javascript

# se pueden definir con el metodo list() o metiendo elementos en un [] y separarlos con comas
my_list = list()
my_other_list = []

print(my_list)
print(my_other_list)

my_list = [23, 34, 54, 21, 43]

print(my_list)

my_other_list = [32, 1.77, "Edgard", True]

print(my_other_list)
print(type(my_other_list))

# En las listas podemos guardar todos los datos primarios como strings, integers, floats, booleans, etc.
# Se puede acceder a sus valores internos

print(my_other_list[2])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])

print(my_list.count(30)) # count() Retorna el numero de ocurrencias de un valor

# Destructuracion de Listas en variables

age, height, name, istrue = my_other_list
print(name)

name, istrue, age, height = my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[1]
print(name)
print(istrue)
print(age)
print(height)

# Se pueden concatenar con el operador + 

print(my_list + my_other_list)


# los tipados en python son dinamicos por lo que cualquier variables aunque fuese una lista se puede reasignar a un string, integer, floats, boolean, etc.
my_list = "Hola Python"
my_list = list("hola") 

print(my_list) # print ["h", "o", "l", "a"]

# se le pueden insertar elementos al final de la lista con el metodo append()
my_list.append("Hello")
print(my_list)

# O en la posicion que quieras con insert()
my_list.insert(1, "Blue")
print(my_list)

# Puedes eliminar un valor de la lista con remove()
my_list.remove("Blue")
print(my_list)

# Puedes eliminar el ultimo elemento de una lista con pop()
# O si le pasas como argumento un indice a pop() el te elimina el elemento que esta en ese indice y lo retorna
popped = my_list.pop()
print(my_list)
print(popped)

# Para vaciar la lista usar el metodo clear()
my_list.clear()
print(my_list)

# Se le puede añadir un nuevo elemento ala lista con notacion de corchetes
my_list.insert(0,"bravo!!")
my_list[0] = "NEw"
print(my_list)

# Puedes copiar una lista con el metodo copy()
my_new_list = my_list.copy()
print(my_list)
print(my_new_list)
print(my_new_list + my_list)

# Se pueden ordenar los valores de una lista alrreves con reverse() 

my_banana = list("banana")
print(my_banana)
my_banana.reverse()
print(my_banana)

# Se puede ordenar una lista con sort()
my_nums = [1, 9, 12, 7, 8]
print(my_nums)
my_nums.sort()
print(my_nums)