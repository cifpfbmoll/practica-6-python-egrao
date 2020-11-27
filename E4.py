# Practica6.py-P6E4
#Escribe un programa que te pida dos numeros, de manera que el segundo sea
#mayor que el primero. El programa termina escribiendo los dos numeros tal y como
# pide:
#Escribe un numero: 6
#Escribe un numero mayor que 6: 6
#6 no es mayor que 6. Vuelve a introducir un numero: 1
#1 no es mayor que 6. Vuelve a introducir un numero: 8
#Los numeros que has escrito son 6 y 8

numero1=int(input("Escribe un numero "))
print("Escribe un numero mayor que", numero1,end=": ")
numero2=int(input())
while (numero1>=numero2):
    print(numero2, "no es mayor que", numero1)
    numero2=int(input("Vuelve a introducir un numero: "))
print("Los numeros que has escrito son",numero1,"y",numero2)