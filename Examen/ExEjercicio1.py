# "ExEjercicio1.py" realizado por Alejandro Martinez (13-10839@usb.ve)
# Ultima modificacion 10:45 a.m.

#Valor incial
Clasificacion = ""

#Se le explica al usuario la funcionalidad del ejercicio
print("A continuacion se le va a pedir que provea tres angulos de un triangulo para decirle si" + \
		"es un triangulo acutangulo, rectangulo u obtusangulo\n\n")

#loop para pedir valores del angulo
while True: 
	try:
		Angulos = [] #Defino mi lista
		for i in range(1,4): #itero tres veces
			Angulos.append(float(input("Valor del angulo " + str(i) + " : "))) #acepto valores float
		assert(all(i > 0 for i in Angulos) and (sum(i for i in Angulos) == 180)) #compruebo que sean mayor a 0 y su suma 180
		break
	except:
		print("\n\nUsted ha introducido un valor incorrecto. Tiene que ser un numero mayor a cero" + \
		 	" tal que la suma de los tres angulos sea igual a 180")
		pass

#Loop que compara cada angulo para verificar que tipo de triangulo es
try:
	for i in Angulos:
		if i > 90:
			Clasificacion = "obtusangulo"
			assert((i - (sum(i for i in Angulos) - i)) > 0) #Resta del angulo mayor de 90 grados menos la suma de los otros dos angulos tiene que ser mayor a 0

		elif i == 90:
			Clasificacion = "rectangulo"
			assert((i - (sum(i for i in Angulos) - 90)) == 0) #Resta del angulo de 90 grados menos la suma de los otros dos angulos tiene que ser igual a 0

		elif (Angulos[0] < 90) and (Angulos[1] < 90) and (Angulos[2] < 90):
			Clasificacion = "acutangulo"
			assert(all( (i < 90) for i in Angulos)) #Asegura que todos angulos sean menor a 90 grados
except:
	print("\n\nHa ocurrido un error, por favor contacte a un tecnico\n\n")
	assert(False)



#Salida
print("\n\nDado los angulos que usted ha introducido, se determina que es un triangulo " + Clasificacion)