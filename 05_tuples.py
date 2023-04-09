# Tuplas ✔

my_tuple = tuple()
my_other_tuple = ()


my_tuple = (28, 1.89, "Edgard", True)
print(my_tuple)
print(type(my_tuple))

# Se puede acceder a los valores de las tuplas como en las listas
print(my_tuple[0])
print(my_tuple[-1])


# Tienen acceso a ciertos metodos de las listas 
print(my_tuple.count("Edgard"))
print(my_tuple.index(True))


# Pero no se pueden reasignar sus valores, las tuplas son constantes
# my_tuple[1] = "Dog" este daria un TypeError ya que no puede ser reasignada


# Sin embargo se pueden concatenar
the_tuple = (2, 4, 5, 5) 
la_tuple = ("Hola", "Bonjour", "Ohayo")

print(the_tuple + la_tuple)

# Puedes recortarla de la siguiente manera
my_sum_tuple = the_tuple + la_tuple
print(my_sum_tuple[2:6])

# Incluso podemos borrar la tupla
del my_sum_tuple
# print(my_sum_tuple) NameError: name 'my_sum_tuple' is not defined