# Practica6.py-P6E11
#Escribir un programa para jugar a adivinar un numero (el ordenador piensa el
#numero y el usuario lo ha de adivinar). El programa empieza pidiendo entre que
#numeros esta el numero a adivinar, se "inventa" un numero al azar y luego el usuario
#va probando valores. El programa va decidiendo si son demasiado grandes o
#pequenyos. pista:
#
#Valor minimo: 0
#Valor maximo: 100
#A ver si adivinas un numero entero entre 0 y 100.
#Escribe un numero: 20
#Demasiado pequenyo Volver a probar: 30
#Demasiado grande Volver a probar: 27
#Correcto Lo has intentado 3 veces.
import random
minimo = int (input ( "Valor minimo:"))
maximo = int (input ( "Valor maximo:"))
secreto = random.randint (minimo, maximo)
print("A ver si adivinas un numero entre %d y %d" %(minimo,maximo))
numero=int(input("Escribe un numero: "))
intentos=1
while numero!=secreto:
    intentos+=1
    if numero>secreto:
        numero=int(input("Demasiado grande. Volver a probar: "))
    else:
        numero=int(input("Demasiado pequenyo. Volver a probar: "))
print("Correcto. Lo has intentado %d veces." %(intentos))
    