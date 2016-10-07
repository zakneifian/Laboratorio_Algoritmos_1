#"Prelab4Ejercicio1.py" Programa realizado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)

#Para ver la utilidad del programa, recurra a /Instrucciones/PreLaboratorio4.pdf y dirijase a la descripcion de Prelab4Ejercicio1.py

#Ultima modificacion: 6 Oct 2016

#Valores iniciales
A = []    #Lista que contendra los 10 enteros
suma = 0  #Variable que contendra la suma de los 10 enteros

#Explicacion al usuario de que hace el programa
print("\nA continuacion introduzca 10 enteros para calcular su suma:\n\n")

#Loop para introducir cada entero en "A"
for i in range(1,11):
	A.append(int(input('Entero numero ' + str(i) + ' :')))

#Precondicion
assert(all (i for i in A if isinstance(i, int) and i !=0 ))

#Loop para sumar cada elemento de "A"
for i in A:
	suma += i

#Postcondicion
assert(suma == sum(i for i in A))

#Salida
print("\n\nLa suma de los 10 enteros es: " + str(suma) + '\n')