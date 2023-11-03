
#COLECCIONES:
"""
Variable que almacena multiples elementos
"""

"""fruta1 = "Manzana"
fruta2 = "Pera"
fruta3 = "Fresa"

Frutas = ["Manzana", "Pera", "Fresa"]"""

#listas, tuplas, diccionarios.
#LISTAS
"""
LISTAS = []
Son mutables: pueden  modificarse.
Son indexadas: posicion de cada elemento de la lista, los indices van de 0 en adelante.
Pueden contener cualquier tipo de datos.
METODOS:
insertar:
append(), insert(indice, elemento).
eliminar:
pop(), remove()
organizar:
sort(), sort(reverse=True)
posicion:
index()
count(): contar elementos.
len(): longitud o cantidad de elementos que contiene la lista.
"""
"""Submodulos = ["Bases de datos", "Nuevas Tecnologias", "Web II", "Metodologias Agiles", "Logica de programación", "Web I", "Moviles"]
#longitud de la lista submodulos
print("La lista contiene",len(Submodulos), "elementos")
#Acceder a un elemento de la lista. se accede teniendo en cuenta la posicion.
print(Submodulos[-1])
#Modificar un submodulo
Submodulos[5] = "Catedra de emprendimiento"
print(Submodulos)
#Insertar elementos:
#Append(elemento): inserta en la ultima posicion de la lista
Submodulos.append("web I")
print(Submodulos)
#insert(posicion, elemento):
Submodulos.insert(4, "Introducción a la programacion")
print(Submodulos)
print(len(Submodulos))
#recorrer lista submodulos:
for elemento in Submodulos:
    print(elemento)
#Recorrer teniendo en cuenta el indice:
for indice in range(len(Submodulos)):
    print(Submodulos[indice], "Esta en la posisicion", indice)

#Eliminar elementos: pop(ndice), remove(elemento), clear()

Submodulos.pop(0)

print(Submodulos)

Submodulos.remove("Web II")

print(Submodulos)

Submodulos.clear()

print(Submodulos)"""

numeros = [1,2,3,4,5,6,7,8,9,-10,11,-12,13,-14,15,2]
#De la lista numeros, almacenar en una nueva lista solo los numeros impares y numeros negativos

imparNegativos = []

for i in range (len(numeros)):
    if numeros[i] < 0 or numeros[i] %2 != 0:
        imparNegativos.append(numeros[i])

print(imparNegativos)

#index(): conocer la posicion del elemeneto

print(numeros.index(2))

#numero de repeticiones del numeros 6:
deportes = ("el numero 6 esta repetido", "baloncesto", "volley", "tenis")

#ordenar lista de forma ascendente: sort()

deportes.sort()
print(deportes)

#ordenar lista de forma descendente: sort(reverse = true)
deportes.sort(reverse=True)
print(deportes)
#recorrer dos o mas listas al tiempo: zip

animales =  ["perro","pajaro","tiburon"]
tipo_animales = ["terrestre", "ave", "Acuatico"]

for A, T in zip(animales, tipo_animales):
    print(f"El {A} es un animal {T}")
