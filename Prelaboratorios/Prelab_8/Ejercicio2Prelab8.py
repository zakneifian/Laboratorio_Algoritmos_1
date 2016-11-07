#'Ejercicio2Prelab8.py' Elaborado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)
#Ultima modificacion a las 8:05 pm 6/nov/2016
#Algoritmo que dados dos valores 'm' y 'n', dependiendo del valor de 'm', efectua distintas operaciones

import sys #Modulo para salir del programa cuando se quiera

#Funcion que explica al usuario el funcionamiento del programa y le pide los valores
def Entrada():
	try:
		print('\nBienvenido, a continuacion introducira sendos valores numericos para m y n.')
		print('Dependiendo del valor de m, se efectuaran distintas operaciones.')
		print('\n------------------\n\nSi m = 10, se efectuara: m/n\nSi m = 5, se efectuara: m*n\nSi m = 3, se efectuara: m + n\nSi m = 2, se efectuara: m^n\nSi m es cualquier otro valor, se devolvera m')
		m = (float(input('\n------------------\n\nm = '))) #asigna el valor de 'm'
		n = (float(input('n = '))) #asigna el valor de 'n'

		assert(isinstance(m, float) and isinstance(n, float)) #asegura que sean numeros float
		return m, n #retorna la tupla (m, n)

	except:
		print('\n------------------\nEl valor que ha introducido ha sido incorrecto. Por favor intente nuevamente.\n------------------')
		Entrada() #Si es invalido, reinicia la funcion

#Funcion que dados dos parametros 'm' y 'n' los opera
def Operacion(m, n):
	#Dependiendo del valor de 'm' efectua distintas operaciones y retorna el resultado
	try:
		if int(m) == 10:
			resultado = m/n
		elif int(m) == 5:
			resultado = m*n
		elif int(m) == 3:
			resultado = m + n
		elif int(m) == 2:
			resultado = m**n
		else:
			resultado = m
		#Aseguramos que tenga un valor correcto todo
		assert(
			   (int(m) == 10 and round(resultado, 2) == round((m/n), 2) ) or \
			   (int(m) == 5  and round(resultado, 2) == round((m*n), 2) ) or \
			   (int(m) == 3  and round(resultado, 2) == round((m+n), 2) ) or \
			   (int(m) == 2  and round(resultado, 2) == round((m**n), 2)) or \
			   (                 round(resultado, 2) == round(m, 2)     )
			  )
		return resultado
	except:
		print("\nHa ocurido un error, iniciemos de nuevo")
		main() #Si hay error, reinicia el programa

#Funcion principal que organiza toda la ejecucion
def main():
	m, n = Entrada() #asigna 'm' y 'n' a los valores de la tupla de la Entrada()
	print("El resultado es ", Operacion(m, n))

	#Le pregunta al usuario si quiere iniciar de nuevo
	empezarDeNuevo = input('\nQuiere usted efectuar otra operacion? (y/n): ').lower() 

	if empezarDeNuevo == 'y': #Si empieza de nuevo, reinicia el programa
		main()
	elif empezarDeNuevo == 'n': #Sino, sale
		sys.exit('\nHasta luego.')
	else:
		sys.exit('\nUsted ha introducido un valor invalido. El programa terminara.') #Si es valor invalido, tambien saldra

#Ejecuta el programa
main()