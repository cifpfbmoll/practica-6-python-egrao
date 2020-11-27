# Practica6.py-P6E3
#Escribe un programa que pida notas y los guarde en una lista. Para terminar de
#introducir notas, escribe una nota que no este entre 0 y 10. El programa termina
#escribiendo la lista de notas.
#Escribe una nota: 7.5
#Escribe una nota: 0
#Escribe una nota: 10
#Escribe una nota: -1
#Las notas que has Escrito son [7.5, 0.0, 10.0]
nota=float(input("Escribe una nota "))
lista=[]
while nota>=0 and nota<=10:
    lista.append(nota)
    nota=float(input("Escribe una nota "))
print("Las notas que has Escrito son",lista)