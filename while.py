
import math
#solicitar al usuario que escoja el area de la figura geometrica que desea

opcion = 0
while opcion != 6:
    print(""" 
    calcular: \n
          \t1. area Triangulo \n
          \t2. area Cudrado \n
          \t3. area rectangulo \n
          \t4. area circulo \n
          \t5. area cubo \n
          \t6. salir \n """)
    opcion =  int(input("ingrese la opcion: "))
    if opcion == 1:
        base=int(input("ingrese la medida de la base en cm del triangulo "))
        altura=int(input("ingrese la medida de la altura en cm del triangulo "))
        total=(base * altura)//2
        print(f"el area del triangulo es {total} cm")
    elif opcion == 2:
        base=int(input("ingrese la medida de la base en cm del cuadrado: "))
        altura=int(input("ingrese la medida de la altura en cm del cuadrado: "))
        total=base * altura
        print(f"el area del cuadrado es {total} cm")
    elif opcion == 3:
        base=int(input("ingrese la medida de la base en cm del rectangulo: "))
        altura=int(input("ingrese la medida de la altura en cm del rectangulo: "))
        total=base * altura
        print(f"el area del rectangulo es {total} cm")
    elif opcion == 4:
        radio = int(input("ingrese la medida en cm del radio "))
        area = math.pi * (radio * radio)
        print(f"el area del triangulo es {area}")
    elif opcion == 5:
        lado=int(input("ingrese un la medida de un lado en cm "))
        areaU= lado *6
        area = areaU *6
        print(f"el area del cubo es")
    else:
        print("bye")

d= 0
while d < 10:
    print(d)
    d+= 1
    if d == 5:
        break

s= 0
while s < 10:
    print(s)
    s+= 1
    if s == 5:
        continue