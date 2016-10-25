'''
Programa realizado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)
Valores inciales:
'N' Representa el numero que se desea trabajar, int
'k' es un valor que se usa para iterar hasta llegar a N el cual es multiplicado por fact, para calcularlo, int
'fact' es el factorial del numero que se esta iterando en el momento, int
'suma' es la sumatoria de todos los factoriales calculados en toda la iteracion, int
'''
import sys 

#Pre: asegura que N sea un valor positivo y que k este entre ese valor y 0

try:
	N = int(input('\n\nEste algoritmo calcula la suma de los factoriales desde 0 hasta N.\n\nA continuacion introduzca el numero: '))
	suma, fact, k = 0,1,0
	assert(N >= 0 and 0<=k<=N)
except:
	print("\nERROR: debe colocar un numero positivo entero mayor o igual a 0")
	print("vuelva a intentarlo \n\nAtt: JK y AM")
	sys.exit()
#Algoritmo
#/////////////////////////////////////////////////////////////

#loop, calcula la sumatoria de factoriales
while k<=N:
	if k>0:
		fact *= k #calcula el factorial del numero que este iterando en el momento
	suma += fact #agrega ese factorial a la suma para completar la sumatoria
	k += 1

#Funcion que definio el profesor que aparece creada por otro en: http://stackoverflow.com/questions/595374/whats-the-python-function-like-sum-but-for-multiplication-product
def prod( iterable ): 
	p= 1 
	for n in iterable: 
		p *= n 
	return p 

#/////////////////////////////////////////////////////////////
#Post
try:
	assert(suma == sum(prod(range(1,i+1)) for i in range(0,N+1)))
except:
	print("\nERROR: Fallo con la verificacion de la sumatoria factorial \nSus desarrolladores pedimos disculpas por las molestias causadas")
#Salida
print("La suma de los factoriales es:", suma, "\n")