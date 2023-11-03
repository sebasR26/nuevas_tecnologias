"""
Diccionario = {}
dinamicos ya que pudenen crecer y decrecer
se trabaja en funcion de la clave 
se trabaja en funcion de la clave. (la clave puede ser unica)

diccionario = {clave: valor}


"""

datos_personales = {"Nombre": "karina",
                    "Apellido": "salazar",
                    "Edad": 38,
                    "Sexo": "femenino"}

print(type(datos_personales))

#otra forma de crear diccionario
"""DatosP = dict(Nombre = "Nayrobi",
              Apellido = "Jimenez",
              Edad = 45,
              Sexo = "Femenino")
print(type(DatosP))"""

#acceder a un elemento 

print(datos_personales["Edad"])

#accerder a un elemento con el metodo get

print(datos_personales.get("Nombre"))

#Modificar un elemento
datos_personales["Apellido"] = "Valencia"

print(datos_personales)

#modificar un elemento inexistente

datos_personales["FNacimiento"] = "36"

print(datos_personales)

#acceder solo a las claves del diccionario sin el metodo key()

for clave in datos_personales:
    print(clave)


#acceder a los valores del diciconario sin el metodo values()

for valor in datos_personales:
    print(datos_personales[valor])

#Obtener clave y valor con el metodo items()

for i,x in datos_personales.items():
    print(f"{i} = {x}")

#pop(clave): elimina un elemento de la clave especifica.,
#popintem(): elimina el ultimo elemento del diccionario,
#clear(): elimina todos los elementos del diccionario

#obtener clave de un diccionario con el metodo key
for v in datos_personales.keys():
    print(v)


#obtener valores de un diccionario con el metodo value

for v in datos_personales.values():
    print(v)

