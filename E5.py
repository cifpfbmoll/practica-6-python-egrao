# Practica6.py-P6E5
#Escribe un programa que te pida numeros cada vez mas grandes y que se guarden 
#en una lista. Para acabar de escribir los numeros, escribe un numero que no sea 
#mayor que el anterior. El programa termina escribiendo la lista de numeros:
#Escribe un numero: 6
#Escribe un numero mayor que 6: 10
#Escribe un numero mayor que 10: 12
#Escribe un numero mayor que 12: 25
#Escribe un numero mayor que 25: 9
#Los numeros que has escrito son: 6, 10, 12, 25  (Comentario si os fijais ya no
#se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto asi a partir de ahora)

numero1=int(input("Escribe un numero "))
print("Escribe un numero mayor que ",numero1,end=": ")
numero2=int(input())
lista=[numero1]
while numero2>lista[-1]:
    lista.append(numero2)
    print("Escribe un numero mayor que", numero2, end=": ")
    numero2=int(input())
print("Los numeros que has escrito son:",end=" ")
for i in range(len(lista)):
    if i==len(lista)-1:
        print(lista[i])
    else:
        print(lista[i],end=", ")
    
