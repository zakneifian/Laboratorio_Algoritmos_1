def Records(Usuario, Nivel):

	with open("Texts/records.txt", "a+") as tablaRecord:
		Condicion1=False
		Condicion2=True	
		#Asignaremos nombre en string a la variable nivel
		nivelstring=""
		if Nivel == "1":
			nivelstring = "Facil"
		elif Nivel == "2":
			nivelstring = "Dificil"
		elif Nivel == "3":
			nivelstring = "Muy-Dificil"
		elif Nivel == "4":
			nivelstring = "Tutorial"

		#Creamos un string que concatene: la cantidad de partidas(partiendo de 1)+nombreUsuario+dificultad
		puntuacion = "1 " + Usuario + " Dificultad: " + str(nivelstring) 
		lista_string_punt = puntuacion.split() #convertimos el string anterior en una lista para manejar la cantidad de partidas en lista
		#Leemos el archivo Records.txt para verificar si tiene o no contenido
		archivo = open("Texts/records.txt", "r")
		contenido = archivo.readlines()
		archivo.close()
		if contenido != []: #si el contenido es distinto de vacio entra al ciclo for
		#iteramos sobre cada linea para ver si existe otra linea que tenga el mismo nombre de usuario y la misma dificultad
			for linea in tablaRecord:
				listalinea=linea.split()
				print(linea) #verificacion
				print(listalinea) #vericacion
				if listalinea[1] == lista_string_punt[1] and listalinea[3] == lista_string_punt[3]: #en caso de existir otra, se le anadira +1 a la cantidad de partidas 
					lista_string_punt[0] = str(int(lista_string_punt[0])+1)
					print("entro al ciclo") #verificacion
					lista_string_punt=' '.join(lista_string_punt) #unimos la lista para que quede en modo string para luego anadirlo al archivo records.txt	
					linea = lista_string_punt
					print(linea) #verificaion (correcto)
					Condicion2=False
				elif Condicion2 == True:
					Condicion1=True
		else:
			tablaRecord.write(puntuacion + "\n")	#le agrega un primer record al archivo

		if Condicion1==True:
			tablaRecord.write(puntuacion + "\n") 	#si no existe una partida con el mismo nombre y dificultad le agrega en una nueva linea el nuevo record
