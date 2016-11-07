#'Ejercicio1Prelab8.py' Elaborado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)
#Ultima modificacion a las 6:21 pm 6/nov/2016
#Algoritmo que una vez escogida una opcion del menu, se piden dos argumentos para operarlos

#Importo sys para usar sys.exit() a futuro
import sys

#Funcion menu
def menu():
	try:
		print("\nBienvenido, a continuacion se le va a ofrecer una lista de opciones\n\n------------------\n")

		print('0) entero + entero') 
		print('1) string + string')
		print('2) lista + lista')
		print('3) entero + string')
		print('4) entero + lista')
		print('5) string + lista')
		print('6) Salir del programa')

		valor = int(input('\n------------------\n\nIntroduzca un numero entero del \'0\' al \'6\' para su escogencia: '))
		assert( any(valor == i for i in range(7)) ) #Se verifica que 'valor' este entre 0 y 6
		return valor #La funcion returna 'valor'
	except:	
		print('\n------------------\nEl valor que ha introducido ha sido incorrecto. Por favor intente nuevamente.\n------------------')
		menu() #Si es invalido, reinicia el menu principal

#Funcion operacion que toma el argumento del valor que retorne el menu
def operacion(val):
	#por cada 'val' (siendo el 'valor' del menu) diferentes casos de como proceder segun la operacion	
	print("\n------------------\n")

	if val == 6: 
		print("\nHasta luego.\n")
		sys.exit()

	try:

		if val == 0:
				arg1 = int(input('A continuacion introduzca el primer entero: '))
				arg2 = int(input('A continuacion introduzca el segundo entero: '))
				resultado = arg1 + arg2

		elif val == 1:
				arg1 = input('A continuacion introduzca su primera cadena de caracteres: ')
				arg2 = input('A continuacion introduzca su segunda cadena de caracteres: ')
				resultado = arg1 + arg2

		elif val == 2:
				arg1 = lista()
				arg2 = lista()
				resultado = arg1 + arg2

		elif val == 3:
				arg1 = int(input('A continuacion introduzca el entero: '))
				arg2 = input('A continuacion introduzca su cadena de caracteres: ')
				resultado = str(arg1) + arg2

		elif val == 4:
				arg1 = [int(input('A continuacion introduzca el entero: '))]
				arg2 = lista()
				resultado = arg2 + arg1
				print(resultado)

		elif val == 5:
				arg1 = [input('A continuacion introduzca su cadena de caracteres: ')]
				arg2 = lista()
				resultado = arg2 + arg1



		assert((val == 0 and isinstance(arg1, int) and isinstance(arg2, int)) or \
			   (val == 1 and isinstance(arg1, str) and isinstance(arg2, str)) or \
			   (val == 2 and isinstance(arg1, list) and isinstance(arg2, list)) or \
			   (val == 3 and isinstance(arg1, int) and isinstance(arg2, str)) or \
			   (val == 4 and isinstance(arg1[0], int) and isinstance(arg2, list)) or \
			   (val == 5 and isinstance(arg1[0], str) and isinstance(arg2, list))
		      )
		return resultado #La funcion retorna el 'resultado'

	except:
		print('\nHa introducido algun valor invalido. Por favor intente nuevamente desde el inicio')
		main() #Si se introduce un valor invalido, el programa comienza desde el inicio

#Funcion que genera listas a partir de un string separadas por '///'
def lista():
	cadena = input('A continuacion introduzca los elementos de su lista separados por un \'///\': ')
	return cadena.split('///') #Usa como separador '///' devolviendo una lista de la cadena separada por eso

#Funcion principal que pone todo en orden
def main():

	val = menu() #Le asigna a 'val' el 'valor' retornado del menu

	print("\n------------------\nEl resultado de su operacion es: ", operacion(val) ) #Imprime la operacion

	empezarDeNuevo = input('\nQuiere usted efectuar otra operacion? (y/n): ').lower() 

	if empezarDeNuevo == 'y': #Si empieza de nuevo, reinicia el programa
		main()
	elif empezarDeNuevo == 'n': #Sino, sale
		sys.exit('\nHasta luego.')
	else:
		sys.exit('\nUsted ha introducido un valor invalido. El programa terminara.') #Si es valor invalido, tambien saldra

#Ejecucion del programa
main()