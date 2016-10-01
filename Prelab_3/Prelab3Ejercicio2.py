#Vars
N = int(input('\n\n\nEste algoritmo calculara la suma de los digitos de un numero entero positivo de 10 digitos maximos.\n\nA continuacion introduzca el numero: '))
suma, cociente, k = 0, N, 0

#Pre
assert(0<N<10000000000)

#Algo
while cociente > 0:
	suma = suma + (cociente%10)
	cociente = cociente//10
	k += 1

#Print
print(N, suma, cociente, k)
print (suma, sum((N//(10**(k-1)))%10 for i in range(0, 11) if (N//(10**(k-1)) != 0))) #revisar

#Post, revisar
assert(suma == sum((N//(10**(k-1)))%10 for (range(0, 11) and (N//(10**(k-1)) != 0))))