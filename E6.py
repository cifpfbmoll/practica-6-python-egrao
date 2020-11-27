# Practica6.py-P6E6
#Escribe un programa que pida primero dos numeros (maximo y minimo) y que despues 
#te pida numeros intermedios. Para terminar de escribir numeros, escribe un numero 
#que no este comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de numeros.
#Escribe un numero: 6
#Escribe un numero mayor que 6: 4
#4 no es mayor que 6. Vuelve a probar: 50
#Escribe un numero entre 6 y 50: 45
#Escribe otro numero entre 6 y 50: 13
#Escribe otro numero entre 6 y 50: 4
#Los numeros situados entre 6 y 50 que has escrito son: 45, 13 
numeroMinimo=int(input("Escribe un numero: "))
print("Escribe un numero mayor que",numeroMinimo,end=": ")
numeroMaximo=int(input())
listaIntermedios=[]
while numeroMaximo<=numeroMinimo:
    print(numeroMaximo,"no es mayor que", numeroMinimo, end=". ")
    numeroMaximo=int(input("Vuelve a probar:"))
print("Escribe un numero entre %s y %s: " %(numeroMinimo,numeroMaximo),end="")
numeroIntermedio=int(input())
while numeroMinimo<numeroIntermedio<numeroMaximo:
    listaIntermedios.append(numeroIntermedio)
    print("Escribe otro numero entre %s y %s: " %(numeroMinimo,numeroMaximo),end="")
    numeroIntermedio=int(input())
print("Los numeros situados entre %s y %s que has escrito son: " %(numeroMinimo,numeroMaximo),end="")
for i in range(len(listaIntermedios)):
    if i==len(listaIntermedios)-1:
        print(listaIntermedios[i])
    else:
        print(listaIntermedios[i],end=", ")
    


    


