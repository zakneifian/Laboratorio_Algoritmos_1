'''

Lab03Ejercicio1.py elaborado por Alejandro Martinez 13-10839@usb

"n" es el numero que se verificara si es o no perfecto, int
"a" es un valor por el cual se ira verificando el modulo y aumentara hasta n-1 en el loop, int
"suma" es el valor total de la suma de todos los valores que toma "a" si cumple n%a, int

'''
#Valores iniciales
n = int(input("\nA continuacion introduzca un numero para verificar si es un numero perfecto: "))
a = 1
suma = 0

#Precondicion: asegura que n sea un numero positivo
assert(n > 0)

#Algoritmo: un loop que si cumple la verificacion suma "a" a la variable "suma"
for i in range(a, n):
	if n%a == 0:
		suma += a
	a += 1

#Postcondicion: asegura que "suma" sea un valor positivo y sea o no "n"
assert(suma > 0 and (suma == n or suma != n))

#Salida, dependiendo del valor de "suma" se compara con "n" para ver si es perfecto
if  suma == n:
	print("\n\nEste numero es perfecto\n\n\n")
else:
	print("\n\nEste numero no es perfecto\n\n\n")

