# Practica6.py-P6E10
#Escribe un programa que te pida los nombres y notas de alumnos.
#Si escribes una nota fuera del intervalo de 0 a 10, el programa 
#entendera que no quieres introducir mas notas de este alumno. Si no 
#escribes el nombre, el programa entendera que no quieres introducir mas 
#alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta 
#estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
#Dame un nombre: Hector Quiroga
#Escribe una nota: 4
#Escribe otra nota: 8.5
#Escribe otra nota: 12
#Dame otro nombre: Ines Valls
#Escribe una nota: 7.5
#Escribe otra nota: 1
#Escribe otra nota: 2
#Escribe otra nota: -5
#Dame otro nombre:
#Las notas de los alumnos son:
#Hector Quiroga: 4.0 - 8.5
#Ines Valls: 7.5 - 1.0 - 2.0
nombreAlumno=input("Dame un nombre: ")
listaAlumnos=[]
stop=""
while nombreAlumno!=stop:
    notaAlumno=float(input("Escribe una nota: "))
    sublista=[nombreAlumno]
    while 0<=notaAlumno<=10:
        sublista.append(notaAlumno)
        notaAlumno=float(input("Escribe otra nota: "))
    listaAlumnos.append(sublista)
    nombreAlumno=input("Dame otro nombre: ")
print("Las notas de los alumnos son: ",listaAlumnos)