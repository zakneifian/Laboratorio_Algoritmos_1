'''

Lab03Ejercicio2.py elaborado por Alejandro Martinez 13-10839@usb


"N" es el numero que se calculara su raiz digital, int
"cociente" es un valor el cual se usa en loops para ir sumando los digitos, int
"suma" es el valor de la sumatoria de los digitos de N, int
"sumatotal" es el valor de la sumatoria de los digitos de suma, int

'''

#Valores iniciales
N = int(input("\nA continuacion introduzca un numero para calcular su raiz digital: "))
cociente = N
suma = 0
sumatotal = 0

#Precondicion: asegura que "N" sea un valor mayor a 0 y como maximo un numero de 10 digitos
assert(0 < N < 10000000000)

#Algoritmo

#calcula la suma de los digitos de "N" y los asigna a "suma"
while cociente > 0:
	suma += cociente%10
	cociente = cociente//10

#calcula la suma de los digitos de "suma" y los asigna a "sumatotal"
while suma > 0:
	sumatotal += suma%10
	suma = suma//10


#Postcondicion
assert(sumatotal > 0 and isinstance(sumatotal, int))

#Salida
print("\n\nLa raiz digital del numero " + str(N) + " es: " + str(sumatotal) + "\n")
