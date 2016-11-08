#Autores: Jesus Kauze 12-10273@usb.ve & Alejandro Martinez 13-10839@usb.ve

#Programa de un juego denominado "Matrix operator" que consiste manipular una matriz 6 x 6 con diferentes propiedades para calcular sumas, porcentajes, valores, posiciones, etc

#los resultados de los valores manipulados seran mostrados en un archivo llamado "report-output.txt"

import time, sys #importamos las librerias necesarias (time: para el tiempo maximo)

#Variables iniciales 

tiempoInicial= time.time()
cota = 0
promedioParesPositivos = 0
promedioRegiones = 0
sumaParesPositivos = 0
sumaImparesNegativos = 0
sumaColumna = 0
sumaFila = 0
sumaRegiones = 0
sumaTemp = 0
contadorParesPositivos = 0
contadorDiagonalSecundaria = 5
contadorFila = 0
contadorColumna = 0
mayorValorPar = -999
menorValorImpar = 999
ListaPromedioColumna = []
ListaPromedioFila = []
ListaSumaRegiones = []
listaPorcentajeRegiones = []

#Leemos el archivo matrix-entry.txt para crear la matriz en una lista
with open('matrix-entry.txt', 'r') as f:
	matriz=[]
	for i in f:
		fila = i.split()
		try:
			#PRECONDICION: Que las lineas de matrix-entry.txt sea igual a las filas de la lista matriz
			assert(i == fila.join(" ") for i in f)
		except:
			print("La matrix ha tenido un error, por favor salga del programa por su salud.")
			sys.exit()
		for j in fila:
			if not isinstance(j, int): #Comprabamos si el elemento tiene un salto de linea al ser no entero
				if j[0] == "-": #en caso de ser negativo tomamos los primeros 2 valores para tomar el negativo
					j = j[:2]
				else: 			#en caso de ser positivo solo tomamos 1 valor 
					j = j[:1] 
		matriz.append(fila) #anexamos los valores a la lista matriz

for i in range(6): #Transformamos los valores de la lista de cadenas a Enteros
	for j in range(6):
		matriz[i][j] = int(matriz[i][j])

#Algoritmo para el Promedio de pares  positivos
for i in range(6):
	if matriz[i][i]%2 == 0 and matriz[i][i] >= 0:
		assert(matriz[i][i]%2 == 0 and matriz[i][i] >= 0)
		contadorParesPositivos += 1
		sumaParesPositivos += matriz[i][i]
	promedioParesPositivos = sumaParesPositivos/contadorParesPositivos
	assert(sum(matriz[i][i]/contadorParesPositivos for i in range(6) if matriz[i][i]%2 == 0 and matriz[i][i] >= 0))

#Algoritmo de la Sumatoria de impares  negativos
for i in range(6):
	if matriz[i][contadorDiagonalSecundaria]%2 != 0 and matriz[i][contadorDiagonalSecundaria] < 0:
		assert(matriz[i][contadorDiagonalSecundaria]%2 != 0 and matriz[i][contadorDiagonalSecundaria] < 0)
		sumaImparesNegativos += matriz[i][contadorDiagonalSecundaria]
	assert(sum(matriz[i][contadorDiagonalSecundaria] for i in range(6) if matriz[i][contadorDiagonalSecundaria]%2 != 0 and matriz[i][contadorDiagonalSecundaria]))
	contadorDiagonalSecundaria -= 1

#Algoritmo para el Mayor y menor elemento de la matriz
for i in range(6):
	for j in range(6):
		if matriz[i][j] % 2 == 0 and mayorValorPar < matriz[i][j]:
			assert(matriz[i][j] % 2 == 0 and mayorValorPar < matriz[i][j])
			mayorValorPar = matriz[i][j]
		elif matriz[i][j] % 2 != 0  and menorValorImpar > matriz[i][j]:
			assert(matriz[i][j] % 2 != 0  and menorValorImpar > matriz[i][j])
			menorValorImpar = matriz[i][j]

#Algoritmo para promedio de los elementos en las filas
for z in range(6):
	sumaFila = 0
	assert(sumaFila == 0) 
	for i in range(6):
		sumaFila += matriz[i][contadorColumna]
	contadorColumna += 1
	ListaPromedioFila.append(sumaFila/6)

#Algoritmo para el Promedio de valores en cada columna
for z in range(6):
	sumaColumna = 0
	for i in range(6):
		sumaColumna += matriz[contadorFila][i]
	contadorFila += 1
	ListaPromedioColumna.append(sumaColumna/6)

#Algoritmo para la Sumatoria de las regiones 3x3
#Region A
for i in range(0, 3): 
	for j in range(0, 3):
		sumaTemp += matriz[i][j]

ListaSumaRegiones.append(sumaTemp)
sumaTemp = 0

#Region B
for i in range(0, 3): 
	for j in range(3, 6):
		sumaTemp += matriz[i][j]

ListaSumaRegiones.append(sumaTemp)
sumaTemp = 0

#Region C
for i in range(3, 6): 
	for j in range(0, 3):
		sumaTemp += matriz[i][j]

ListaSumaRegiones.append(sumaTemp)
sumaTemp = 0

#Region D
for i in range(3, 6): 
	for j in range(3, 6):
		sumaTemp += matriz[i][j]

ListaSumaRegiones.append(sumaTemp)

#Algoritmo para el Promedio de la sumatoria de las subregiones
for i in ListaSumaRegiones:
	promedioRegiones += i/4

#Algoritmo para los Porcentajes de la sumatoria de las subregiones
for i in ListaSumaRegiones:
	sumaRegiones += i

for i in ListaSumaRegiones:
	listaPorcentajeRegiones.append(str(round((100*i/sumaRegiones), 3)) + "%")

#Salida al archivo report-output.txt
with open("report-output.txt", "w") as salida:
	salida.write("El promedio de pares positivos es: " + str(promedioParesPositivos))
	salida.write("\nLa sumatoria de los numeros impares negativos es: " + str(sumaImparesNegativos))
	salida.write("\nEl promedio de los numeros pares positivos es: " + str(promedioParesPositivos))
	salida.write("\nEl mayor elemento par es: " + str(mayorValorPar) + "\nEl menor elemento impar es: " + str(menorValorImpar))
	for i in range(6):
		salida.write("\nEl promedio de la fila " + str(i + 1) + " es: " + str(ListaPromedioFila[i]))
	for i in range(6):
		salida.write("\nEl promedio de la columna " + str(i + 1) + " es: " + str(ListaPromedioColumna[i]))
	for i in range(4):
		salida.write("\nEl valor de la suma de la sub-region " + str(i + 1) + " es: " + str(ListaSumaRegiones[i]))
	salida.write("\nEl promedio de la sumatoria de las sub-regiones es: " + str(promedioRegiones))
	for i in range(4):
		salida.write("\nEl porcentaje de la sub-region " + str(i + 1) + " con respecto a la suma de todas las sub-regiones es: " + str(listaPorcentajeRegiones[i]))

#POST del report-output.txt el post tiene que verificar que en el archivo report para cada linea cumpla con cada una de las post o resultados de cada algoritmo

#Interaccion con el usuario para buscar el valor en la posicion (X,Y)
print("Bienvenido a Matrix Operator \nA continuacion se trabajara un matriz del archivo matrix-entry.txt\nUd. Podra ver el valor de cualquier elemento colocando las posiciones X y luego Y.")
print("Tambien dada la matriz 6*6 en el archivo \"matrix-entry.txt\" se devolveran datos trabajados en el archivo \"report-output.txt\"")

while cota <= 1000: #utilizamos funcion COTA para limitar el numero de veces posibles
	try:
		cota+=1
		valormenu=input("\nIntroduzca '1' Para calcular una posicion o introduzca cualquier otro valor para salir de matrix operator: ")
	#------------- Verificamos que el tiempo actual UNIX menos el tiempo inicial calculado sea menor que 360 seg. sino sale del programa con sys.exit()
		if time.time() - tiempoInicial >= 360:
			print("Ha excedido su tiempo en la Matrix")
			break
	#-------------
		if valormenu == "1":
			X = int(input("\nA continuacion inserte el valor de la coordenada X (fila entre 1 y 6)   : "))
	#------------- Verificamos que el tiempo actual UNIX menos el tiempo inicial calculado sea menor que 360 seg. sino sale del programa con sys.exit()
			if time.time() - tiempoInicial >= 360:
				print("Ha excedido su tiempo en la Matrix")
				break
	#-------------
			Y = int(input("\nA continuacion inserte el valor de la coordenada Y (columna entre 1 y 6): "))
	#------------- Verificamos que el tiempo actual UNIX menos el tiempo inicial calculado sea menor que 360 seg. sino sale del programa con sys.exit()
			if time.time() - tiempoInicial >= 360:
				print("Ha excedido su tiempo en la Matrix")
				break
	#-------------
			print("\nEl valor del elemento es: " + str(matriz[X-1][Y-1]))
		else:
			print("Gracias por usar el matrix operator")		
			break
		assert(1<=X<=6 and 1<=Y<=6)
	except:
		print("ERROR")

sys.exit("\nUsted ha excedido su tiempo (6 minutos) o numero de intentos (1000) o ha decidido salir del programa")