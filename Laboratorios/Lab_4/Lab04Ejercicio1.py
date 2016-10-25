# Lab04Ejercicio1 hecho por Alejandro Martinez 13-10839@usb.ve

#Valor inicial de M
M = int(input("Introduzca la cota superior del grado del polinomio: "))

#Precondicion
assert(M >= 0)

#Valor inicial de la lista donde almacenare los coeficientes del polinomio
lista = []

#loop que agrega el valor del coeficiente y lo pone junto a la x con su respectivo grado y lo une a la lista
for i in range(0, M + 1):
	valor = input("Introduzca el valor de C" + str(i) + ": ") + "X^" + str(i) + " + "
	if valor == "0X^" + str(i) + " + ": 
		break
	else:
		lista.append(valor)

#Postcondicion
assert(len(lista) <= M + 1)


#Salida
print("\n\nEl grado del polinomio es: " + str(len(lista) - 1))
print("P(X) = " + str(lista))
