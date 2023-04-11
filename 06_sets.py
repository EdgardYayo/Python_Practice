# Sets ✔

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Edgard", "Pazos", 28, 1.77}
print(type(my_other_set))
print(my_other_set)

my_new_set = set("Edgard")
print(my_new_set)
print(len(my_new_set)) # len() para saber cuentos elementos tiene el set

# Con add() podemos añadir un nuevo elemento al set
my_new_set.add("hello")
print(my_new_set) # Un set no es una estructura ordenada

# En un set cada elemento solo puede estar una vez (no admite repetidos)
my_new_set.add("hello")
print(my_new_set)

# Se puede comprobar si un elemento existe en un set con el operador "in"
print("hello" in my_new_set)
print("he" in my_new_set)

# Se puede eliminar un elemento del set con el metodo remove()
my_new_set.remove("hello")
print(my_new_set)

# Se puede borrar todo el set con clear()
my_new_set.clear()
print(my_new_set)

# Se pueden unir dos sets con el metodo union()
first_set = {"Hola", "Hello"}
second_set = {"Bonjour", "Ohayo"}

print(first_set.union(second_set))
print(first_set.union({"Hii", "dd"}))

# Para saber las diferencias entre elementos de los sets con el metodo difference()
setty = first_set.union(second_set)
print(setty.difference(first_set))