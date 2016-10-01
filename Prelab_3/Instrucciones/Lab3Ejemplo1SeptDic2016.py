#

# Lab3Ejemplo1.py

#

# DESCRIPCION: Programa que dado un número N,

# calcula la sumatoria de los números pares entre 0 y N-1. 

# Dicho sumatoria 

# es almacenada en suma.

#

# Versión de: 

#	Prof. Josué Ramírez

#

# Ultima modificacion: 29/09/2016

#

#

# CONSTANTES:

#	N: int // Límite superior del rango de enteros pares a sumar

N=10


# VARIABLES:

#	i: int // Valor que permite recorrer los enteros entre 0 y N

#	suma: int // Valor de la sumatoria de los enteros pares entre 0 y N



# Valores iniciales:

i,suma=0,0


# Precondicion: 

assert(N > 0 and 0<=i<=N)

while ( i <= N ):
   print("i vale:",i)
   if (i % 2 == 0):
      suma=suma+i 
   i=i+1
     

# Postcondicion: 
 
assert(N > 0 and i > N)

 # Salida:

print("La sumatoria de enteros pares de 0 a",N,"es:")

print(suma)
