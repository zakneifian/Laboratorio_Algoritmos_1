#"Lab07Ejercicio2.py" elaborado por Alejandro Martinez (13-10839@usb.ve)
#Ultima modificacion 10:26 am (1/nov/2016)
#Este programa gestiona datos de "calculo-nomina-usb.tx" y los imprime en "nomina-trabajadores-usb.txt"

#Valores iniciales
lineas = []
HorasTotales = 0
MontoTotal = 0

#Si no existe el archivo, arroja error
try:
	with open("calculo-nomina-usb.txt", "r") as entrada:
			for line in entrada:
				lineas.append(line.split())
except:
	print("Usted no tiene el archivo calculo-nomina-usb.txt")
	assert(False)

#loop que suma las horas totales y calcula el monto total
for i in range(len(lineas)):
	try:
		HorasTotales += int(lineas[i][2])
		MontoTotal += (int(lineas[i][2]) * float(lineas[i][3]))

		assert(0 <= int(lineas[i][2]) <= 744 and float(lineas[i][3]) > 0)
	except:
		print("La linea " + str(i) + " no cumple con el formato valido. Se seguiran evaluando las demas.")

#Salida del archivo
with open("nomina-trabajadores-usb.txt", "w") as salida:
	salida.write("Cantidad-Horas: " + str(HorasTotales))
	salida.write("\nMonto-Total: " + str(MontoTotal))

#Postcondicion
assert((HorasTotales == sum(int(lineas[i][2]) for i in range(1, len(lineas)))) and \
	   (MontoTotal   == sum((int(lineas[i][2]) * float(lineas[i][3])) for i in range(1, len(lineas))))
	  )