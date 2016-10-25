#

# Lab1Ejercicio2.py

#

# DESCRIPCION: Dados tres valores enteros a,b,c que cumplen a>=b>=c, intercambie los valores de manera que cumplan a<=b<=c

#

# Autor: 

#	Estudiante Alejandro Martínez 13-10839@usb.ve

#

# Valores iniciales:

a = 3

b = 2

c = 1

# Precondicion: 

assert((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)) and (isinstance(c,int) or isinstance(c,float)) and a>=b>=c)



# Calculos:

a,c = c,a	



# Postcondicion: 

assert(a<=b<=c)



#Output
print("El resultado es: ")
print("a = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c))
