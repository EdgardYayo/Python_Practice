# # Working directorys ✔
from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft ---> Windows
# /usr/local/bin ---> Mac


# Relative path
# ..\carpeta\archivo.py ---> Windows
# ../carpeta/archivo.py ---> Mac

# EJEMPLOS DE USO

path = Path(".")  # <---- Se le pasa como argumento una ruta de un path o un archivo

# Metodo que retorna True o False si el path existe o no
# print(path.exists())

# Metodo que crea el path
# print(path.mkdir())

# Metodo que elimina el path
# print(path.rmdir())

# Metodo que busca algo especifico en el path
# print(path.glob("*.py")) <----- Toma un argumento que es a traves de que patron va buscar
# Por ejemplo aqui buscaria todos los archivos de python con terminacion .py 

# Por ejemplo para imprimir todos los archivos python en el directorio actual se utiliza la siguiente expresion
for file in path.glob("*.py"):
    print(file)