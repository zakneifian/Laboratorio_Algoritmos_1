# "PreLab06Ejercicio1.py" hecho por Jesus Kauze (12-10273@usb.ve) y Alejandro Martinez (13-10839@usb.ve) 
import sys
#Programa que verifica si un numero entero es perfecto, abundante, o deficiente

#Variables:
verificacion= 0 
numero=0

#Funcion que lee la entrada de datos
def Entrada():
	#PRE: var > 0 
	#POST: True
	var=int(input("Ingrese un numero de maximo 9 digitos: "))
	return var

#Funcion que valida los datos ingresados
def Validacion(n):
	try:
		assert(n>0) #precondicion
	except:
		print("solo se aceptan enteros positivos mayores a 0")
		sys.exit() #salimos del programa en caso de que no se cumpla el pre
	#Post: True
	
#funcion del algoritmo
def Algoritmo(x):
	#pre: x>0
	#post:(numero ==(sum(i for i in range(1,n) if n%i==0)
	numero=0
	for i in range(1,x):
		if x%i==0: #si es divisor dicho numero se almacena en la variable numeros
			numero= numero + i  
			print(i)
		else:
			pass
	if numero == x:
		print("\nes perfecto")
	elif numero < x:
		print("\nes defectivo")
	elif numero > x:
		print("\nes abundante")
	else:
		pass

n=Entrada()
Validacion(n)
Algoritmo(n)
#ciclo de la funcion Algoritmo(n)

for i in range(1,n):
	if n%i==0:
		numero= numero + i
	else:
		pass

	  
#POSTCONDICION
try:
    assert ((numero ==(sum(i for i in range(1,n) if n%i==0))))
    print("\nel programa corre perfecto")
except:
    print("hubo un error en el programa lo sentimos")