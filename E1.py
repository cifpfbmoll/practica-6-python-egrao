# Practica6.py-P6E1
#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de
#introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la
#lista de palabras.
palabra=str(input("Escribe una palabra "))
lista=[]
while palabra!="":
    lista=lista+[palabra]
    palabra=str(input("Escribe mas palabras "))
print("Las palabras que has Escrito son",lista)