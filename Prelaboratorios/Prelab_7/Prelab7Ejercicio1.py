# "Prelab7Ejercicio1.py" elaborado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)
# Programa que multiplica el numero por la palabra en un 'input.txt' y lo devuelve al 'output.txt'
# Ultima modificacion 12:50 a.m. 29/oct/2016

import re       #Importo RegEx
lista = []      #Creo una lista vacia donde almacenar el contenido del output

with open('input.txt', 'r') as file: #Abro input.txt con 'r' lectura y lo llamo file, una vez termine el bloque, se cierra
		for line in file:            #Para cada linea de texto en el archivo
			try:
				number = int(re.search(r'-?[0-9]+', line).group())  #El entero del string del match (.group()) de la busqueda (.search()) r"-?[0-9]+"  http://i.imgur.com/yDqNWbq.png (el r"" es raw data)
				word   = re.search(r'\b[ATCG]+\b', line).group()    #El string del match (.group()) de la busqueda (.search()) r"\b[ATCG]+\b" http://i.imgur.com/yDqNWbq.png (el r"" es raw data)
				assert(number >= 0 and 0 <= len(number*word) < 50 ) #Aseguro que el numero sea no negativo y que la longitud de la palabra exista (si tiene caracteres fuera de actg no existe) y menor a 50
				lista.append(number*word + '\n')                    #Si es asegurado, se añade el multiplo del # por la palabra mas el caracter de nueva linea
			except:
				lista.append('Linea erronea\n') #Sino, se añade ese string mas el caracter de nueva linea

with open('output.txt', 'w') as file: #Abro/creo output.txt con 'w' escritura y lo llamo file, una vez termine el bloque, se cierra
	for item in lista:                #Por cada objeto en la lista
		file.write(item)              #Escribo ese objeto en el archivo, que con el \n, se separan lineas