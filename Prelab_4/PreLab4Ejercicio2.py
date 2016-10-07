#"Prelab4Ejercicio2.py" Programa realizado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)

#Para ver la utilidad del programa, recurra a /Instrucciones/PreLaboratorio4.pdf y dirijase a la descripcion de Prelab4Ejercicio2.py

#Define la clase concursante
class Concursante:
	def __init__(self, Nombre, Cantidad):
		self.Nombre = Nombre  #Nombre del concursante
		self.Cantidad = Cantidad #Cantidad de hamburguesas ingeridas por el concursante

#Le pregunta al usuario cuantos concursantes hay en su lista
N = int(input("\nEste programa devolvera en orden de mayor a menor a los ganadores del evento.\n\nA continuacion introduzca la cantidad de concursantes en la lista: "))
grupo = []

#Precondicion
assert(N > 0)

#Le pregunta al usuario el nombre y cantidad de hamburguesas ingeridas de cada Concursante
for i in range(1, N + 1):
	grupo.append(
				 Concursante(input("\nIntroduzca el nombre del Concursante numero " + str(i) + " en la lista: ") ,\
				 int(input("Introduzca la cantidad de hamburguesas ingeridas del Concursante numero " + str(i) + " en la lista: ")))
				)

#Redefiniendo el grupo de tal forma que se ordena de mayor a menor en funcion de la cantidad de hamburguesas ingeridas
grupo = sorted(grupo, key=lambda Concursante: Concursante.Cantidad, reverse = True)

#Postcondicion
assert(
		all(len(grupo[i].Nombre) > 0 and grupo[i].Cantidad >= 0  for i in range(0, N)) and\
		grupo == sorted(grupo, key=lambda Concursante: Concursante.Cantidad, reverse = True)
	  )

#Salida
print('\n\n\nEl/La ganador/a es ' + grupo[0].Nombre + ' con ' + str(grupo[0].Cantidad) + ' hamburguesas ingeridas')
print('Le siguen:')
for i in range(1,N):
	print(grupo[i].Nombre + ' con ' + str(grupo[i].Cantidad) + ' hamburguesas ingeridas')