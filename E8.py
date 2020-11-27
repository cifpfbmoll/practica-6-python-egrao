# Practica6.py-P6E8
#Escribe un programa que te pida primero un numero y luego te
#pida numeros hasta que la suma de los numeros introducidos coincida 
#con el numero inicial. El programa termina escribiendo la lista de numeros.
#Escribe limite: 50
#Escribe un valor: 10
#Escribe otro valor: 45
#45 es demasiado grande. Escribe otro valor: 1
#Escribe otro valor: 39
#El limite a alcanzar es 50. La lista creada es: 10, 1, 39
limite=int(input("Escribe un limite: "))
valor1=int(input("Escribe un valor: "))
#valor2=int(input("Escribe otro valor: "))
lista=[valor1]
#while sum(lista)>limite:
#    print("%s es demasiado grande. Escribe otro valor: " %(valor2),end="")
#    valor2=int(input())
#    suma=sum(lista)
while sum(lista)!=limite:
 #   valor2=int(input("Escribe"))
    valor2=int(input("Escribe otro valor: "))
    lista.append(valor2)
    while sum(lista)>limite:
        lista.remove(valor2)
        print("%s es demasiado grande. Escribe otro valor: " %(valor2),end="")
        valor2=int(input())
        lista.append(valor2)
    print("")
print("El limite a alcanzar es %s. La lista creada es: " %(limite),end="")
for i in range(len(lista)):
    if i==len(lista)-1:
        print(lista[i])
    else:
        print(lista[i],end=", ")
