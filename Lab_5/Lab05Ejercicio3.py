#Autor Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion: 18-oct-2016 11:00 am
##"Lab05Ejercicio3.py"

#Se imprime la descripcion del problema
print("Si se toma cualquier número natural x, el siguiente de la secuencia se genera asi: si el número x es par, el siguiente numero sera igual a la mitad x; si el numero x  es impar, el siguiente se obtiene al multiplicar por 3 y sumarle 1. Si el proceso se repite, en algun numero finito de pasos se llegara a la secuencia 4, 2, 1")

#Se le pide al usuario que introduzca un valor correcto para la comprobacion
while True:
	try:
		n = int(input("A continuacion introduzca un numero positivo entero: "))
		assert(n > 0  and n % 1 == 0)
		break
	except:
		print("Introduzca un valor valido")

#Se empieza la lista con el valor introducido
lista = [n]

#loop con cota que verifica si es 4, otro numero par o un numero impar y hace el respectivo proceso
for i in range(99999999999999999999999999999999):
	print("\n\nEl numero de elementos de la lista es: " + str(len(lista)))
	print("El ultimo numero actual de la lista es: " + str(lista[i]))
	if lista[i] == 4: #Si es 4
		break
	elif lista[i] % 2 == 0: #Si es par
		lista.append(lista[i]/2)
	else: #Si es impar
		lista.append((lista[i] * 3) + 1)

try: #El assert verifica en cada caso de si es par o impar que el siguiente numero se cumpla
	assert(all(lista[i] == 2*lista[i + 1] for i in range(len(lista) - 1) if (lista[i]%2 == 0)) and \
		   all(lista[i] == (lista[i + 1] - 1)/3 for i in range(len(lista) - 1) if (lista[i]%2 != 0))
		  )
	print("\nEl programa ha imprimido la secuencia correctamente")
except:
	print("\nHubo un error en el programa")