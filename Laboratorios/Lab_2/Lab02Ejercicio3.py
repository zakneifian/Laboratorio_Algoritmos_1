edad = 12 #determina la edad, entero
gpa = 4.8 #determina el promedio, float

#Precondicion que determina que el promedio este entre 0 y 5 y tenga una edad mayor a 0 y menor a 120
assert(0 < edad < 120 and 0 <= gpa <= 5 and isinstance(edad, int) and isinstance(gpa, float))

gpa = round(gpa, 2) #elimina el error de calculo de float binario y redondea gpa a un maximo de 2 decimales

if edad > 18:
	if 4.5 <= gpa <= 5:
		beca = 2000
	elif 4.1 < gpa < 4.5:
		beca = 1000
	elif 3 <= gpa <= 3.9:
		beca = 500
	else: #Los que tienen menor a 3 o tienen entre 4 y 4.1
		beca = 0

else: #edad < 18
	if 4.5 <= gpa <= 5:
		beca = 3000
	elif 4.1 < gpa < 4.5:
		beca = 2000
	elif 3 <= gpa <= 3.9:
		beca = 100
	else: #Los que tienen menor a 3 o tienen entre 4 y 4.1
		beca = 0

if beca > 0:
	print("El estudiante ha sido otorgado con una beca de $" + str(beca))

elif beca == 0:
	print("El estudiante no ha sido otorgado ninguna beca, envie invitacion")

#Postcondicion
assert(beca >= 0) #asegura que la beca tenga un valor mayor o igual a 0 para 
#				   que tenga sentido el programa y devuelva el print