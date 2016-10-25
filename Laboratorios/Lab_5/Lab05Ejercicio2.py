#Autor Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion: 18-oct-2016 11:10 am
#"Lab05Ejercicio2.py"

#Defino una lista vacia
secuencia = []

#En el loop itero hasta una cota grande
for i in range(0, 1000000):
	if i == 0: #En la primera iteracion imprimo estas lineas
		print("\n\nEste programa va a verificar si la lista de numeros enteros no negativos esta ordenada de menor a mayor.")
		print("Use el numero \"0\" para terminar de introducir numeros")
		print("La secuencia no puede estar vacia, por ende el primer numero no puede ser 0")

	try: #Se pide un valor no negativo
		valor = int(input("A continuacion introduzca un valor no negativo: "))
		if valor == 0: #Si es 0, termina el loop
			break
		else: #Sino, lo agrega y verifica las condiciones pedidas, que el inicial sea distinto de 0, que sea no negativo, entero y que la secuencia no sea vacia
			secuencia.append(valor)
		assert((secuencia[0] != 0) and (secuencia[i] > 0) and (secuencia[i] % 1 == 0) and (0 < len(secuencia) < 1000000))
	except:
		print("Has introducido un valor invalido. Recuerde que tiene que ser entero no negativo y el inicial distinto de 0")

try: # imprimimos que esta ordenada si cumple la condicion
	assert(all(secuencia[i] < secuencia[i+1] for i in range(len(secuencia) - 1)))
	print("La lista esta ordenada")
except: #Sino imprimimos que no esta ordenada
	print("La lista no esta ordenada")