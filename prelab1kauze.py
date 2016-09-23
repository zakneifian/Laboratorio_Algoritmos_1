import math
#Nombramos las variables A, B, C pidiendole al usuario que introduzca su valor

A = int(input("introduzca el valor de A "))

B = int(input("introduzca el valor de B "))

C = int(input("introduzca el valor de C "))

assert(A !=0)

while 4*A*C > B*B:
	print("")
	print("Error: numero imaginario \nintroduce valores nuevamente")
	print("")
	A = int(input("introduzca el valor de A "))

	B = int(input("introduzca el valor de B "))

	C = int(input("introduzca el valor de C "))

	assert(A !=0)

raiz= math.sqrt(B*B - 4*A*C)
X1= ((-1)*B + raiz)/2*A
X2= ((-1)*B - raiz)/2*A
print("")
print("La primera raiz del polinomio es: ")
print(X1)
print("")
print("La segunda raiz del polinomio es: ")
print(X2)