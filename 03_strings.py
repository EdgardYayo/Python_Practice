# Strings (Cadenas de Texto o Caracteres)

my_string = "Hola string"
my_other_string = 'Hola other string'

# Calculando la longitud de los strings con len()

print(len(my_string))
print(len(my_other_string))

# Strings con salto de linea
my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

# Strings con tabulacion 
my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

# Con doble barra \\ se escapa a los saltos de linea y las tabulaciones
my_escape_string = "\\t Este es un string con \\n escape"
print(my_escape_string)


# Formateo

# %s para meter strings
# %d para meter integers
# %f para meter float

name, surname = "Edgard", "Pazos"
print("Mi nombre es {} {}".format(name, surname))
print("Mi nombre es %s %s" %(name, surname))
print(f"Mi nombre es {name} y me apellido {surname}")

# Desempaquetado de caracteres en un string

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("---------------------")

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])


# Division de caracteres

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Built In functions of Python for Strings

print(language.capitalize()) # Vuelve la primera letra de cada palabra en mayuscula
print(language.upper()) # Vuelve todas las letras mayusculas
print(language.count("t")) # Cuenta cuantas letras ahi de las que recibe como parametro
print(language.isnumeric()) # Devuelve true o false dependiendo si el string es un numero o no
print(language.lower()) # Vuelve todas las letras minusculas

# Algunos otros

# isupper() devuelve true o false dependiendo si las letras son mayusculas o no
# startswith("parametro") devuelve true o false si el string comienza con los caracteres que recibe como parametro
