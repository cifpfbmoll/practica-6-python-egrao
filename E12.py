# Practica6.py-P6E12
#Escribir un programa para jugar a adivinar un numero (el usuario piensa un numero y
#el programa lo ha de adivinar). El programa empieza pidiendo entre que numeros
#esta el numero a adivinar y luego intenta adivinar de que numero se trata. El usuario
#va diciendo si el numero que ha dicho el programa es menor, mayor o igual al que se
#ha buscado.
#Valor minimo: 0
#Valor maximo: 100
#Piensa un numero entre 0 y 100 a ver si lo puedo adivinar.
#Es 50 ?: mayor
#Es 75 ?: menor
#Es 62 ?: menor
#Es 56 ?: mayor
#Es 59 ?: igual
#Gracias por jugar!!
#Mejoras (opcionales):
# que al principio el programa se asegure de que el valor maximo es superior al
#valor minimo.
# Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le
#decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir que
#estamos haciendo trampas y debe dejar de jugar con nosotros.
import random
minimo=int(input("Dime el valor minimo: "))
maximo=int(input("Dime el valor maximo: "))
randomNumero = random.randint (minimo, maximo)
print("Piensa un numero entre %d y %d a ver si lo puedo adivinar." %(minimo, maximo))
print("Es %d?" %(randomNumero), end="")
respuesta=str(input())
while respuesta!="igual":
    while respuesta=="mayor":
        minimo=randomNumero
        randomNumero = random.randint (minimo, maximo)
        print("Es %d?" %(randomNumero), end="")
        respuesta=str(input())
    while respuesta=="menor":
        maximo=randomNumero
        randomNumero = random.randint (minimo, maximo)
        print("Es %d?" %(randomNumero), end="")
        respuesta=str(input())
print("Gracias por jugar!")