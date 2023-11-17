#Funciones
#funciones tradicionales

"""
def nombre_funcion(parametro(opcionales)):
    bloque de codigo
    return

nombre_funcion(argumentos) #llamado de la funcion


"""

#funcion sin argumentos y sin return

"""def saludo():
    print("Hola Mundo")

print(saludo())"""

#funcion con un solo paramatro y sin return

"""def name(nombre):
    print(f"{nombre} es un estudiante hiperactivo, pero participa")

name("Sebastian")"""

#funcion con varios parametros:
#calcular el promedio de 2 notas:

"""def promedio(n1, n2):
    prom = (n1 + n2) / 2
    return prom

print(promedio(1,5))
print(promedio(3,5))"""

#funciones con parametros predeterminados:
#funcion multiplique 3 valores:
"""def multi(a, b=4, c=8,):
    return a*b*c

print(multi(2,1))"""

"""def suma(d,e,f):
    return d+e+f

print(suma(2,9,40))"""

#parametros de longitud variable: *args
"""def multiplicar(*num):
    resultado = 1
    for i in num:
        resultado *= i
    return resultado

print(multiplicar(1,20,3,4,9,15))"""

#funcione para filtrar de una lista numerica solo los numeros impares


"""numeros = [1,2,3,4,5,6,7]

def impar(*num):
    lista = []
    for num in numeros:
        if num%2!=0:
            lista.append(num)
            
    return lista

print(impar(numeros))"""

#lambda

numeros = [1,2,3,4,5,6,7,8,9,10]

nuevaLista = filter(lambda x: x%2!=0, numeros)

print(list(nuevaLista))
