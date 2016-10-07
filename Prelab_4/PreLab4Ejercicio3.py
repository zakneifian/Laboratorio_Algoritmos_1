#"Prelab4Ejercicio3.py" Programa realizado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)

#Para ver la utilidad del programa, recurra a /Instrucciones/PreLaboratorio4.pdf y dirijase a la descripcion de Prelab4Ejercicio3.py

#Define la clase estudiante
class Estudiante:
	def __init__(self, Edad, Nombre, Indice):
		self.Edad = Edad
		self.Nombre = Nombre
		self.Indice = Indice

#Le pregunta al usuario cuantos estudiantes hay en su lista
N = int(input("\nEste programa calculara el promedio de la edad del grupo y el promedio del indice.\n\nA continuacion introduzca la cantidad de estudiantes en la lista: "))
grupo = []

#Precondicion
assert(N > 0)

#Le pregunta al usuario la edad, nombre e indice de cada estudiante
for i in range(1, N + 1):
	grupo.append(
				 Estudiante(int(input("\nIntroduzca la edad del estudiante numero " + str(i) + " en la lista: ")),\
				 input("Introduzca el nombre del estudiante numero " + str(i) + " en la lista: ") ,\
				 float(input("Introduzca el indice del estudiante numero " + str(i) + " en la lista: ")))
				)

#Definiendo los promedios
PromedioEdad = round((sum(grupo[i].Edad for i in range(0, N)))/float(N), 4)
PromedioIndice = round((sum(grupo[i].Indice for i in range(0, N)))/float(N), 4)

#Postcondicion
assert(
		all(grupo[i].Edad > 0 and grupo[i].Edad > 0 and len(grupo[i].Nombre) for i in range(0, N)) and\
		PromedioEdad == round((sum(grupo[i].Edad for i in range(0, N)))/float(N), 4) and\
		PromedioIndice == round((sum(grupo[i].Indice for i in range(0, N)))/float(N), 4)
	  )

#Salida
print("\n\n\nEl promedio de la edad es: " + str(PromedioEdad) + "\n\nEl promedio del indice es: " + str(PromedioIndice))