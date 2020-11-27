# Practica6.py-P6E13
#Desarrolla de nuevo el ejercicio de la practica anterior 
#de los numeros primos, con while. Reflexiona y escribe en 
#el propio programa en forma de comentario, que opcion es mejor
#y por que.
#Escribe un programa que pida un numero y escriba si primo o no
#Dame un numero: 123
#El numero 123 no es primo
#Dame un numero:127
#El numero 127 es primo
numero=int(input("Dame un numero: "))
divisor=2
primo=True
#while numero%divisor!=0 and 1<divisor<numero:
if numero%divisor==0 and numero!=2:
    primo=False
while divisor<numero and numero%divisor!=0:
    divisor+=1
    if numero%divisor==0 and divisor<numero:
        primo=False
if primo:
    print("El numero %d es primo" %(numero))
else:
    print("El numero %d no es primo" %(numero))

#Este metodo es mucho mas eficiente puesto que el bucle while una vez encuentra 
#un solo numero, diferente de 1 o del input, que sea divisor lo marca como NO primo
#y termina el programa. El bucle for seguiria haciendo la comprobacion de si todos
#los numeros hasta el input son divisores a pesar de que ya se ha cumplido la condicion
#para que el numero no sea primo. Por ello, para este problema en concreto, un
#bucle while es mas eficiente.
