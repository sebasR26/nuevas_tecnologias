import math


opcion = 0
while opcion != 8:
    print(""" 
    calcular: \n
          \t1. suma \n
          \t2. resta \n
          \t3. multiplicacion \n
          \t4. divicion \n
          \t5. potencia \n
          \t6. factorial \n
          \t7. Raiz cuadrada \n
          \t8. salir \n """)
    opcion =  int(input("ingrese la opcion: "))
    if opcion == 1:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        total = num1 + num2 
        print(f"total = {total}")
    elif opcion == 2:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        total = num1 - num2 
        print(f"total = {total}")
    elif opcion == 3:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        total = num1 * num2 
        print(f"total = {total}")
    elif opcion == 4:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        if num1 == 0 or num2 == 0:
            print("no puedes ingresar 0 bro")
        else:
            total = num1 // num2 
            print(f"total = {total}")
        
        
    elif opcion == 5:
        num1 = int(input("ingrese el numero base: "))
        num2 = int(input("ingrese el numero exponente: "))
        total = pow(num1,num2) 
        print(f"total = {total}")
    elif opcion == 6:
        num= int(input("ingrese el numero: "))
        total=math.factorial(num)
        print(f"total = {total}")
    elif opcion == 7:
        num= int(input("ingrese el numero: "))
        if num <= 0:
            print("bro solo numeros positivos")
        else:
            total=math.isqrt(num)
            print(f"total = {total}")
    else:
        print("bye")