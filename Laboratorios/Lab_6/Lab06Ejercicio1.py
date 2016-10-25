# "Lab06Ejercicio1.py" hecho por Alejandro Martinez 13-10839@usb.ve
# Ultima modificacion: 25 Oct 2016 9:00 a.m.
# Este programa recibe coeficientes e imprime un polinomio en notacion polinomial

#Valor inicial de cota
M = int(input("Introduzca la cota superior del grado del polinomio: "))
lista = []


#Valor inicial de la lista donde almacenare los coeficientes del polinomio


#loop que agrega el valor del coeficiente y lo pone junto a la x con su respectivo grado y lo une a la lista
def HacedorPolinomio(cota):

	#Precondicion
	assert(cota >= 0)

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

def CalcGrado(cota):
	
	#Precondicion
	assert(len(lista) > 0)

	grado = str(len(lista) - 1)
	print("\n\nEl grado del polinomio es: " + grado)

	#Postcondicion
	assert(len(lista) <= cota + 1)


#Salida
def main():

	Polinomio = ""
	for i in HacedorPolinomio(M):
		Polinomio += i
	print("\n\nP(X) = " + Polinomio)

	CalcGrado(M)

main()