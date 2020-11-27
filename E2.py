# Practica6.py-P6E2
#Escribe un programa que te pida numeros y los guarde en una lista. Para terminar
#de introducir numero, simplemente escribe Salir. El programa termina escribiendo
#la lista de numeros.
#Escribe un nombre: 14
#Escribe una otro nombre: 123
#Escribe una otro nombre: -25
#Escribe una otro nombre: 123
#Escribe una otro nombre: Salir
#Los numeros que has escrito son [14, 123, -25, 123]
lista=[]
nombre=str(input("Escribe un nombre "))
while nombre!="Salir":
    lista.append(nombre)
    nombre=str(input("Escribe una otro nombre "))
print("Los numeros que has escrito son",lista)