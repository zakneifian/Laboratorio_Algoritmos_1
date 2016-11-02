#"Lab07Ejercicio1.py" elaborado por Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion 10:07 am (1/nov/2016)
#Este programa gestiona datos de "datos-dace.txt" y los imprime en "reporte-dace.txt"

#Variables iniciales
lineas = []
promedio = 0
menor91 = 0
mayor91 = 0
masculinos = 0
femeninos = 0

#intenta abrirlo, sino existe, arroja error despues
try:
	with open("datos-dace.txt", "r") as archivo:
		for line in archivo:
			lineas.append(line.split())
except:
	print("Usted no tiene el archivo datos-dace.txt")
	assert(False)

#Loop que suma el promedio y cuenta todo lo demas
for i in range(len(lineas)):
	try:
		promedio += float(lineas[i][3])/(len(lineas)-1)

		if int(lineas[i][0][:2]) < 91:
			menor91 += 1

		elif int(lineas[i][0][:2]) > 91:
			mayor91 += 1

		if lineas[i][4] == "M":
			if float(lineas[i][3]) > 3.5:
				masculinos += 1

		elif lineas[i][4] == "F":
			if float(lineas[i][3]) > 4.0:
				femeninos += 1
		assert(0 <= float(lineas[i][3]) <= 5 and 0 < int(lineas[i][0][:2]) < 100 and (lineas[i][4] == "M" or lineas[i][4] == "F"))
	except:
		print("La linea " + str(i) + " no cumple con el formato valido. Se seguiran evaluando las demas.")

#Se abre el archivo en escritura y se imprime lo demas
with open("reporte-dace.txt", "w") as salida:
	salida.write("El promedio de los indices es: " + str(promedio))
	salida.write("\nCantidad de estudiantes con carnet menor a 91: " + str(menor91))
	salida.write("\nCantidad de estudiantes con carnet mayor a 91: " + str(mayor91))
	salida.write("\nCantidad de estudiantes masculinos con indice superior a 3.5: " + str(masculinos))
	salida.write("\nCantidad de estudiantes femeninos con indice superior a 4.0: " + str(femeninos))

#Postcondicion
assert((promedio == sum(float(lineas[i][3])/(len(lineas) - 1) for i in range(1, len(lineas)))) and \
	   (0 <= menor91 + mayor91 <= (len(lineas) - 1))
	  )