#
# Ejemplo1.py
#
# DESCRIPCION: Programa que dados tres enteros a,b y c,
# calcula la division de a*a entre (b-c). Dicho resultado
# es almacenado en d.
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 6/04/2014
#

# VARIABLES:
#	a: int // Valor cuyo cuadrado sera el dividendo
#	b: int // Parte del divisor
#	c: int // Parte del divisor
#	d: float // Resultado de la division

# Valores iniciales:
a = 25
b = 10
c = 25
	
# Precondicion: 
assert((b-c) != 0)

# Calculos:
d = a**2 / (b-c)	

# Postcondicion: 
assert(d ==(a*a)/(b-c))

# Salida:
print("El resultado es ")
print(d)