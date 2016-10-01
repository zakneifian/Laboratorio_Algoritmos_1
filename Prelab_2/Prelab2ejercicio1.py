'''
 Autores: Alejandro Martinez 13-10839@usb.ve
		  Jesus Kauze		 12-10273@usb.ve

Prelab2Ejercicio1.py

Variables a usar:

A: Constante que acompana a x**2
B: Constante que acompana a x
C: Constante independiente
x1: raiz 1 de x
x2: raiz 2 de x
'''

# Explicacion al usuario de la funcionalidad del programa
print("\n========================================================\n\n\n" + \
	"Este programa hallara las raices de la ecuacion de segundo grado Ax^2 + Bx + C." + \
	"A continuacion por favor introduzca enteros para los valores de A, B y C:")

# Dado las especificaciones del problema, pido un int de cada constante A, B, C.
A = int(input('\nIntroduzca valor del numero A: '))
B = int(input('\nGracias, ahora por favor introduzca el valor de B: '))
C = int(input('\nExcelente, por ultimo introduzca el valor de C: '))

# Pre: aseguramos el filtro pedido
assert((A != 0) and (4*A*C <= B*B))

#Como uso el discriminante dos veces, prefiero calcularlo solo una vez bajo la formula ((b^2 - 4ac)^1/2)
discriminante = (B*B - 4*A*C)**0.5

#Calculo las raices de forma separada
x1 = (-B + discriminante) / (2*A)
x2 = (-B - discriminante) / (2*A)

#Post: compruebo que "A*x1*x1 + B*x1 + C" y "A*x2*x2 +B*x2 + C" son casi iguales a 0.
#	por motivos de error del float, compruebo truncando x1 y x2 a 4 cifras decimales significativas
#	Todo por error de aproximacion del float.
assert(float(format(A*x1*x1 + B*x1 + C, "0.4f")) == 0 and float(format(A*x2*x2 +B*x2 + C, "0.4f")) == 0)

#Le dejo saber al usuario cuales son las raices de su polinomio
print("\n\n========================================================\n\nLas raices del polinomio " + str(A) + "X^2 + " + str(B) + "X + " + str(C) + " son:\n\n X1 = " + str(x1) + "\n X2 = " + str(x2))

#Nota, por problemas computacionales de como se cuenta binariamente, los valores float no son totalmente 
#exactos, por lo tanto, tuve que limitar x1 y x2 truncandolos con 4 cifras significativas para que dieran el mas amplio repertorio
#de respuestas, sin comprometer cifras usables. Aun asi, para valores como A = 3, B = 1000000, C = 3, el programa no pasa el post.
#Esto, de nuevo reitero, es debido a las limitaciones computacionales. para que funcione de esta manera tendria que limitar las
#cifras significativas a 3 decimales, comprometiendo el uso del programa. Para demas valores como inclusive A = 3, B = 100000, C = 3, 
#el problema da el resultado sin ningun problema