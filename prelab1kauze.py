# DESCRIPCION: Programa que posee un Algoritmo para calcular las

# raíces del polinomio "AX^2 + BX + C"


# Autor: 

#	Jesus Kauze		12-10273


# VARIABLES:

#	A: int // Valor de A en "AX^2 + BX + C"

#	B: int // Valor de B en "AX^2 + BX + C"

#	C: int // Valor de C en "AX^2 + BX + C"

# Valores iniciales:

import math
#Entrada A, B, C pidiendole al usuario que introduzca su valor

A = int(input("introduzca el valor de A: "))

B = int(input("introduzca el valor de B: "))

C = int(input("introduzca el valor de C: "))
 
#Verificamos la PreCondicion

assert((A != 0) and (4 * A * C <= B * B)

#Algoritmo

raiz = math.sqrt(B*B - 4*A*C)

X1 = (-B + raiz) / (2*A)
X2 = (-B - raiz) / (2*A)

#Verificamos la PostCondicion

assert((A * X1 * X1 + B * X1 + C == 0) and (A * X2 * X2 + B * X2 + C == 0))

#Salida

print("")
print("La primera raiz del polinomio es: ")
print(X1)
print("")
print("La segunda raiz del polinomio es: ")
print(X2)
