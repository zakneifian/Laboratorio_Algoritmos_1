#

# Lab1Ejercicio1.py

#

# DESCRIPCION: Programa que dado el radio, calcula el área de una circunferencia

#

# Autor: 

#	Estudiante Alejandro Martínez 13-10839@usb.ve


# Valores iniciales:

pi = 3.1415 # valor aprox de pi

r = 3 #Inicializando variable
	

# Precondicion: 

assert(pi ==3.1415 and (isinstance(r,int) or isinstance(r,float)))



# Calculos:

Area = pi*r*r	

# Postcondicion: 

assert(Area == pi*r*r)

# Salida:

print("El resultado es ")

print(Area)
