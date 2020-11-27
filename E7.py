# Practica6.py-P6E7
#Escribe un programa que pida un numero (limite) y luego te pida 
#numeros hasta que la suma de los numeros introducidos supere el lImite
#inicial. El programa termina escribiendo la lista de numeros.
#Escribe limite: 50
#Escribe un valor: 10
#Escribe otro valor: 25
#Escribe otro valor: 7
#Escribe otro valor: 14
#El limite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos numeros es: 56
limite=int(input("Escribe un limite: "))
valor1=int(input("Escribe un valor: "))
lista=[valor1]
suma=valor1
#suma=sum(lista)
while limite>suma:
    valor2=int(input("Escribe otro valor: "))
    lista.append(valor2)
    suma+=valor2
    #valor1=int(input("Escribe otro valor: "))
print("El limite a superar es %d. La lista creada es " %(limite),end="")
for i in range(len(lista)):
    print(lista[i], end=", ")
print("ya que la suma de estos numeros es:", suma)
    
    
    


