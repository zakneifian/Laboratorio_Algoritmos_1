#"modo" le dice al usuario si quiere encriptar o desencriptar
modo = int(input("\nSi quiere encriptar, introduzca 1.\nSi quiere desencriptar, introduzca 2.\n\nQuiero: "))

#"n" es la llave
n = int(input("Introduzca el valor de la llave, debe ser un valor entero entre 1 y 26: "))

#Precondicion
assert( 1 <= n <= 26 and (modo == 1 or modo == 2))

#lista con el alfabeto y espacio
alfabeto = [" ", 'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Le pregunta al usuario el string y lo regresa y lo pone en minusculas
string = input("\nIntroduzca la oracion a trabajar: ")
string = string.lower()

#Funcion para encriptar 
def encriptar(string):
	string2 = "" #defino una variable local que almacenara mi string
	for i in string: #loop que iterara letra por letra del string
		for j in range(0, len(alfabeto)): #loop que iterara los indices del alfabeto
			if i == " ": #Si es " " lo agrega y rompe el loop
				string2 = string2 + i
				break
			elif i == alfabeto[j]: #si la letra es igual a una del alfabeto,
				i = alfabeto[(j + n)%26] #le suma la llave y le saca el modulo de 26 que es el numero de letras en el abecedario
				string2 = string2 + i #le suma i al string local
				break #termina el loop
	return string2

def desencriptar(string):
	string2 = "" #defino una variable local que almacenara mi string
	for i in string: #loop que iterara letra por letra del string
		for j in range(0, len(alfabeto)): #loop que iterara los indices del alfabeto
			if i == " ": #Si es " " lo agrega y rompe el loop
				string2 = string2 + i
				break
			elif i == alfabeto[j]: #si la letra es igual a una del alfabeto,
				i = alfabeto[(j - n)%26] #le resta la llave y le saca el modulo de 26 que es el numero de letras en el abecedario
				string2 = string2 + i #le suma i al string local
				break #termina el loop
	return string2


#Salida
if modo == 1:
	print("\n\nEl string encriptado es: " + encriptar(string) + "\n\n\n")
elif modo == 2:
	print("\n\nEl string encriptado es: " + desencriptar(string) + "\n\n\n")