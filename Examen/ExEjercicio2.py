# "ExEjercicio2.py" elaborado por Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion 11:00 almacene

#Valor inicial
lista = []
suma = 0

#Le explica al usuario la funcionalidad del programa
print("\nSe le va a ir pidiendo precios de un mismo producto a lo largo del tiempo para calcular su promedio.\n")

#loop que va agregando valores a la lista
for i in range(0, 999999999999999999):		
		valor = float(input("Valor " + str(i) + " del producto: "))
		assert(isinstance(valor, float)) #asegura que no haya omitido introducir valor al comprobar que es un valor float
		if valor == 0: 
			break
		else:
			lista.append(valor)

#Precondicion
assert((len(lista) > 0) and all(i > 0 for i in lista)) #asegura que la lista no este vacia y que no haya elementos negativos en ella

#loop que calcula la suma de todos los valores
for i in lista:
	suma += i

promedio = suma/len(lista)

#Postcondicion
assert(promedio == sum(i for i in lista)/len(lista))

#Salida
print("\n\nEl promedio de sus productos es " + str(promedio))