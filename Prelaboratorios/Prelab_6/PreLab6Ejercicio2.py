# "PreLab06Ejercicio2.py" hecho por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)
# Ultima modificacion: 25 Oct 2016 5:00 p.m.
# Este programa recibe coeficientes e imprime un polinomio en notacion polinomial

#Valor inicial de cota
M = int(input("Introduzca la cota superior del grado del polinomio: "))
lista = [] #Valor inicial de la lista donde almacenare los coeficientes del polinomio


#Funcion que construye el polinomio en una lista
def HacedorPolinomio(cota):

	#Precondicion: Que la cota sea mayor a 0
	assert(cota > 0)

	#loop que agrega el valor del coeficiente y lo pone junto a la x con su respectivo grado y lo une a la lista
	for i in range(0, cota + 1):
		if i == 0: #En el valor inicial solo pone el coeficiente sin X
			valor = input("Introduzca el valor de C" + str(i) + ": ")
			assert(len(valor) > 0) #asegura que no haya omitido introducir valor
			if valor == "0":
				print("\n\nEl polinomio no puede estar vacio\n\n")
				assert(False) #saca del programa
		else: #Para cualquier otro i en el rango, agrega " + CiX^i"
			valor = " + " + input("Introduzca el valor de C" + str(i) + ": ") + "X^" + str(i)
			assert(len(valor) > 5) #asegura que no haya omitido introducir valor
		if valor == " + " + "0X^" + str(i): #Si se introduce el 0, se para el loop sin agregarlo
			break
		else: #Sino, se agrega a la lista
			lista.append(valor)

	#Postcondicion: asegura que la longitud de la lista sea congruente con la cota y que ningun valor de la lista sea 0
	assert((len(lista) <= cota + 1) and all(i != (" + " + "0X^" + str(i)) for i in lista))

	return lista #La funcion devuelve una lista

def CalcGrado(cota): #Funcion que calcula el grado de un polinomio
	
	#Precondicion
	assert(len(lista) > 0) #Que la longitud de la lista no sea vacia

	grado = str(len(lista) - 1) #la longitud total menos el coeficiente inicial da el grado.
	print("\n\nEl grado del polinomio es: " + grado)

	#Postcondicion: asegura que la longitud de la lista sea congruente con la cota
	assert(len(lista) <= cota + 1)


#Salida
def main(): #Funcion principal

	Polinomio = "" #String donde se pondra el polinomio
	for i in HacedorPolinomio(M): #loop que suma cada string de la lista
		Polinomio += i 
	print("\n\nP(X) = " + Polinomio)

	CalcGrado(M)

main() #Ejecucion del programa