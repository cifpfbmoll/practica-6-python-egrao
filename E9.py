# Practica6.py-P6E9
#Escribe un programa que te pida nombres de personas y sus numeros 
#de telefono. Para terminar debe pulsar S cuando te pida el nombre. 
#El programa termina escribiendo nombres y numeros de telefono. Nota: 
#La lista en la que se guardan los nombres y numeros de telefono tiene 
#esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
#Dame un nombre: Pepe Gonzalez
#Dame el telefono: 971971971
#Dame un nombre: Macarena Gomez
#Dame el telefono: 971999999
#Dame un nombre: Pascual Ribot
#Dame el telefono: 666555444
#Dame un nombre: S
#Los nombres y telefonos de la agenda son:
#Pepe Gonzalez: 971971971
#Macarena Gomez: 971999999
#Pasqual Ribot: 666555444
nombre=input("Dame un nombre: ")
lista_nombreTlf=[]
stop="S"
if nombre==stop:
    print("Los nombres y telefonos de la agenda son:", lista_nombreTlf)
while nombre!=stop:
    tlf=int(input("Dame el telefono: "))
    sublista=[nombre,tlf]
    lista_nombreTlf.append(sublista)
    nombre=input("Dame un nombre: ")
    if nombre==stop:
        print("Los nombres y telefonos de la agenda son:")
        for i in range(len(lista_nombreTlf)):
            for j in lista_nombreTlf[i]:
                print([j])
