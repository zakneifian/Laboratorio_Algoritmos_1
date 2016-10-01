import sys
#Vars
N = int(sys.argv[1])
suma, cociente = 0, N

#Pre
assert(0<N<10000000000)

#Algo
print('\n\n\nEste algoritmo calculara la suma de los digitos de un numero entero positivo de 10 digitos maximos.')
while cociente > 0:
	suma = suma + (cociente%10)
	cociente = cociente//10

#Post, revisar
assert(suma == sum((N//(10**(i)))%10 for i in range(0, 11) if (N//(10**(i)) != 0)))

#Salida
print("El valor de la suma es:", suma)