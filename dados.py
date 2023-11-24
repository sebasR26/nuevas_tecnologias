"""Escriba un programa que muestre una partida de dados entre dos jugadores, se debe
ingresar la cantidad de turnos que se van a jugar, cada jugador tira un dado. Si un jugador
saca un valor mayor que el otro, gana los puntos de ambos dados. Si los dos jugadores
sacan el mismo valor, ninguno recibe puntos. Si en el ultimo turno hay un empate, esos
puntos se pierden y termina la partida. Debe mostrar quien gana la partida, quien gana
cada turno y la puntuación acumulada por cada jugador.
Para el examen pueden usar la librería random (import random) y utilizar el método
random.randint(desde, hasta) que toma números enteros de forma aleatorias según rango
dado."""

"""import random

p1 = 0;
p2 = 0;

turnos = int(input("ingrese la cantidad de turnos:  "))

for i in range(turnos):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"el jugador uno saco: {dado1}")
    print(f"el jugador dos saco: {dado2}")
    if dado1 > dado2:
        p1 = dado1 + dado2
        print("el jugador uno gano la partida")
    elif dado2 > dado1:
        p2 = dado1 + dado2
        print("el jugador dos gano la partida")
    elif dado1 == dado2:
        print("mala suerte")

print(f"la puntuacion del jugador uno es: {p1}")
print(f"la puntuacion del jugador dos es: {p2}")

if p1 > p2:
    print("el jugado 1 gano la partida")
elif p2 > p1:
    print("el jugador 2 gano la partida")"""

#crear una funcion lamba que calcule la factorial de un numero

import math


num= int(input("ingrese el numero: "))
print(lambda num: math.factorial(num))





    
    