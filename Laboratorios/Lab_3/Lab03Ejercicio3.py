'''

Lab03Ejercicio3.py elaborado por Alejandro Martinez 13-10839@usb


"dia" es la cantidad de dias que elige el usuario en algun determinado mes, int
"mes" es la cantidad de meses que elige el usuario, int
"dinero" es la cantidad de dinero que se ganaria por dia, int
"suma" es la sumatoria de "dinero" en el rango de los dias totales
"var" es una variable que toma distintos valores a lo largo del algoritmo como "mes" y "dia" para trabajar loops

'''
#Valores iniciales
dia = int(input("\nA continuacion introduzca un numero para el dia: "))
mes = int(input("\nA continuacion introduzca un numero para el mes: "))
dinero = 3
suma = 0
var = mes

#Precondicion asegura que el valor de dia y mes tenga sentido
assert((mes == 2 and 1 <= dia <= 29) or \
	 ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and 1 <= dia <= 30) or \
	 ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and 1 <= dia <= 31))

#Algoritmo


#transforma los meses a dias
while var > 1:
	if var == 2:
		dia += 29
	elif var == 4 or var == 6 or var == 9 or var == 11:
		dia += 30
	elif var == 3 or var == 5 or var == 7 or var == 8 or var == 10 or var == 12:
		dia += 31
	var -= 1

#asigna la variable a la cantidad actual de dias
var = dia

# calcula la cantidad de dinero por dia y la suma a "suma"
while var > 0:
	suma += dinero
	dinero *= 2
	var -= 1

#Salida
print("\n\nEl acumulado de dinero es " + str(round(suma/100.0, 2)) + " pesos\n")

#Post: asegura que "suma" sea el valor de la sumatoria de 0 a dia de la cantidad de dinero inicial por 2 elevado al dia actual
assert(suma == sum((2**i)*3 for i in range(0,dia)))