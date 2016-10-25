# "Lab06Ejercicio2.py" hecho por Alejandro Martinez 13-10839@usb.ve
# Ultima modificacion: 25 Oct 2016 9:00 a.m.
# Este programa recibe coeficientes e imprime un polinomio en notacion polinomial

#Valor inicial de cota
M = int(input("Introduzca la cota superior del grado del polinomio 1: "))
N = int(input("Introduzca la cota superior del grado del polinomio 2: "))
operador = input("Introduzca un operador aritmetico: ")
lista1 = []
lista2 = []


#Valor inicial de la lista donde almacenare los coeficientes del polinomio


#loop que agrega el valor del coeficiente y lo pone junto a la x con su respectivo grado y lo une a la lista
def HacedorPolinomio(lista, cota):

	#Precondicion
	assert(cota >= 0)
	print("\n\nA continuacion introduzca los valores del polinomio:\n")
	for i in range(0, cota + 1):
		if i == 0:
			valor = input("Introduzca el valor de C" + str(i) + ": ")
			assert(len(valor) > 0) #asegura que no haya omitido introducir valor
			if valor == "0":
				print("\n\nEl polinomio no puede estar vacio\n\n")
				assert(False) #saca del programa
		else:
			valor = " + " + input("Introduzca el valor de C" + str(i) + ": ") + "X^" + str(i)
			assert(len(valor) > 5) #asegura que no haya omitido introducir valor
		if valor == " + " + "0X^" + str(i): 
			break
		else:
			lista.append(valor)

	#Postcondicion
	assert((len(lista) <= cota + 1) and all(i != (" + " + "0X^" + str(i)) for i in lista))

	return lista

def Operacion(lista1, lista2):

	#Precondicion
	assert(len(lista1) > 0 and len(lista2) > 0)

	Polinomio1 = ""
	for i in lista1:
		Polinomio1 += i

	Polinomio2 = ""
	for i in lista2:
		Polinomio2 += i

	Polinomio3 = "(" + Polinomio1 + ")" + operador + "(" + Polinomio2 + ")"

	#Postcondicion
	assert(operador == "+" or operador == "-" or operador == "*" or operador == "/")
	return Polinomio3



#Salida
def main():
	print(Operacion(HacedorPolinomio(lista1, M), HacedorPolinomio(lista2, N)))

main()