#Autor Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion: 18-oct-2016 9:30 am
#"Lab05Ejercicio1.py"

#Importamos el modulo sys
import sys

#Valores iniciales
a = 1
suma = 0

while True: #Se pide que se introduzca un valor que cumpla la condicion
	try:
		n = int(input("\nA continuacion introduzca un numero natural para verificar si es un numero perfecto, deficiente o abundante: "))
		assert(n > 0 and n % 1 == 0) #asegura que n sea un numero positivo y entero
		break
	except:
		print("Introduzca un valor valido para \"n\". Recuerde, tiene que ser Natural y mayor a 0.")


#Algoritmo: un loop que si cumple la verificacion, suma "a" a la variable "suma"
try:
	for i in range(a, n):
		if n%a == 0:
			suma += a
		a += 1
	assert(suma == sum(i for i in range(1, n) if n%i == 0)) #asegura que "suma" sea la suma de los "i" en el rango de 1 hasta n-1 si n%1 es 0
except:
	print("El programa tiene un problema, acuda a un programador.")
	sys.exit() #Aborta el programa

#Salida
if suma == n:
	print("\n\nEste numero es perfecto\n\n\n")
elif suma > n:
	print("\n\nEste numero es abundante\n\n\n")
else: # suma < n
	print("\n\nEste numero es deficiente\n\n\n")

