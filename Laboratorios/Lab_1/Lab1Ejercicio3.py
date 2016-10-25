#

# Lab1Ejercicio3.py

#

# DESCRIPCION: Dice si b es par


# Autor: 

#	Estudiante Alejandro Martínez 13-10839@usb.ve

# Valores iniciales:

b = 1234567890

	

# Precondicion: 

assert(isinstance(b,int) or isinstance(b,float))



# Calculos:

if b%2 == 0:
	t = True
else:
	t = False

# Postcondicion: 

assert((b%2 == 0 and t == True) or (b%2!=0 and t==False))



# Salida:
if t == True:
	print("Es par")
else:
	print("No es par")
