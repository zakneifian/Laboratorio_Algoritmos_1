#"Prelab4Ejercicio3.py" Programa realizado por Alejandro Martinez (13-10839@usb.ve)

#Ultima modificacion: 11 Oct 2016

#Define la clase estudiante
class Estudiante:
		Edad = 0    # Edad del estudiante
		Nombre = "Nombre" # Nombre del estudiante
		CI2611_p1 = 0 # CI2611_p1 del estudiante
		CI2611_p2 = 0 # CI2611_p1 del estudiante
		Indice = 0 #Nota del 1 al 5 de CI2611

#Le pregunta al usuario cuantos estudiantes hay en su lista
N = int(input("\nEste programa calculara el promedio de la edad del grupo y el promedio del indice.\n\nA continuacion introduzca la cantidad de estudiantes en la lista: "))
grupo = [Estudiante() for x in range(1, N + 1)] #lista donde se almacenaran los Estudiantes con su respectiva Edad, Nombre e Indice academico

#Precondicion
assert(N > 0)

#Le pregunta al usuario el nombre, edad, notas de parciales en cada estudiante y calcula el indice
for i in grupo:
	i.Nombre    =     input("\nCual es el nombre del estudiante: ")
	i.Edad      = int(input("Cual es la edad de " + i.Nombre + ": "))
	i.CI2611_p1 = int(input("Cual es la nota de " + i.Nombre + " en el primer parcial de CI2611: "))
	i.CI2611_p2 = int(input("Cual es la edad de " + i.Nombre + " en el segundo parcial de CI2611: "))
	if 85 <= i.CI2611_p1 + i.CI2611_p2 <= 100:
		i.Indice = 5
	elif 70 <= i.CI2611_p1 + i.CI2611_p2 < 85:
		i.Indice = 4
	elif 50 <= i.CI2611_p1 + i.CI2611_p2 < 70:
		i.Indice = 3
	elif 30 <= i.CI2611_p1 + i.CI2611_p2 < 50:
		i.Indice = 2
	elif  0 <= i.CI2611_p1 + i.CI2611_p2 < 30:
		i.Indice = 1
	else:
		print("La suma de los parciales tiene valores no definidos en el programa")



#Definiendo los promedios
PromedioP1 = round((sum(grupo[i].CI2611_p1 for i in range(0, N)))/float(N), 4)
PromedioP2 = round((sum(grupo[i].CI2611_p2 for i in range(0, N)))/float(N), 4)

#Postcondicion
assert(
		all((grupo[i].Edad > 0) and (0<= grupo[i].CI2611_p1 <= 50) and (0<= grupo[i].CI2611_p2 <= 50) and (len(grupo[i].Nombre) > 0) and (0 <= grupo[i].Indice <= 5) for i in range(0, N)) and\
		PromedioP1 == round((sum(grupo[i].CI2611_p1 for i in range(0, N)))/float(N), 4) and\
		PromedioP2 == round((sum(grupo[i].CI2611_p2 for i in range(0, N)))/float(N), 4)
	  )

#Salida
for i in grupo:
	print("\nLa nota de " + i.Nombre + " es: " + str(i.Indice))
print("\n\nEl promedio del parcial 1 es: " + str(PromedioP1))
print("El promedio del parcial 2 es: " + str(PromedioP2) + "\n\n")