# Lists ✔ son como arreglos en Javascript

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
