"""
arreglos inmutables: no se pueden modificar
tuplas = ()
las tuplas tambien se pueden representar con elementos separados por comas
tuplas = elemento1, elmento2, elemnto3.....
tuplas de solo elemento tambien debe llevar copa
tuplas = elemento,

"""

"""tuplas = 3,
print(type(tuple))

Dias_semana = "Lunes", "Martes", "Miercoles"
print(type(Dias_semana))"""

"""

metododos no compatibles: pop(), insert(), insert(), remove(), sort(),
append(),

para poder usarlos debes convertir la tupla en listas

"""

# meses = ("enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Octubre", "Noviembre", "Diciembre")

"""print(meses[2])

meses[3] = "super" #error porque las tuplas son inmutables"""

#print(meses)

#index

#print(meses.index("Octubre"))

#longitud de la tupla

#print(len(meses))


"""numeros = (1,2,3,4,5,6,7,8,9,10,1,1,2)

#cuantas repeticiones tiene el numero 6

contar = numeros.count(6)

print(contar)"""

#concatenar tuplas

pares = (2,4,6,8,10)
impares = (1,3,5,7,9) 

concatenarTuplas = pares + impares

"""print(concatenarTuplas)
print(impares)"""

#concatenar ordenando
#conversion a lista

"""listcombinada = list(impares)+list(pares)
listcombinada.sort()


print(listcombinada)"""

#concatenar ordenando

conca = list(pares + impares)
conca.sort()
tuplaO=tuple(conca)
print(tuplaO)
    