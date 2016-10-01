# Programa realizado por Jesus Kauze (12-10273@usb.ve) y Alejandro Martinez (13-10839@usb.ve) 

#Importamos la biblioteca sys
import sys

#Variables iniciales
#'N' es el numero el cual se trabajara en el algoritmo, int
#'suma' es la suma de cada digito del numero N, int
#cociente toma el valor de N el cual cambiara alrededor del algoritmo, se usa para ir reduciendo su valor en el loop y dejar N tranquilo, int
N = int(sys.argv[1])
suma, cociente = 0, N

#Pre, aseguramos que N tenga un valor mayor a 0 pero como maximo un numero de 10 digitos
assert(0  < N< 10000000000)

#Algo
#/////////////////////////////////////////////////////////////

#explicacion
print('\n\n\nEste algoritmo calculara la suma de los digitos de un numero entero positivo de 10 digitos maximos.')

#loop que va sumando cociente%10 mientras que cociente sea mayor a 0, este loop se itera el numero de digitos que tenga N
while cociente > 0:
	suma = suma + (cociente%10)
	cociente = cociente//10
#/////////////////////////////////////////////////////////////

#Post, asegura que la suma sea la correcta
assert(suma == sum((N//(10**(i)))%10 for i in range(0, 11) if (N//(10**(i)) != 0)))

#Salida
print("El valor de la suma es:", suma)