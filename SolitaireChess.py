#Librerias a importar
import pygame, time, sys, eztext
from pygame.locals import *

#Inicializamos pygame
pygame.init() 

#Frames per second de la ventana
FPS = 9
fpsClock = pygame.time.Clock()

#Ancho y largo de la ventana que se generara
display_width  = 760
display_height = 760

#Creamos la ventana y le damos nombre
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('USB\'s Solitaire Chess')

#Cargamos el icono y lo asignamos a la ventana
iconoPNG = pygame.image.load('Sprites/icono.png') 
pygame.display.set_icon(iconoPNG)

#Colores
white = (255,255,255)
black = (0  ,0  ,0  )
red   = (255,0  ,0  )
green = (0  ,255,0  )
blue  = (0  ,0  ,255)

#Fuente de letra
Font = pygame.font.SysFont(None, 30)

#Carga de sprites
Dificultad       = pygame.image.load('Sprites/Dificultad.png'	  )
CargadoTablero 	 = pygame.image.load('Sprites/CargadoTablero.png' )
DesafioTeclado	 = pygame.image.load('Sprites/DesafioTeclado.png' )
Opcionesfacil 	 = pygame.image.load('Sprites/OpcionesFacil.png'  )
OpcionesDificil	 = pygame.image.load('Sprites/OpcionesDificil.png')
Leyenda			 = pygame.image.load('Sprites/Leyenda.png'		  )
TableroPNG       = pygame.image.load('Sprites/Tablero.png'        )
ReyPNG           = pygame.image.load('Sprites/Rey.png'            )
DamaPNG         = pygame.image.load('Sprites/Reina.png'           )
AlfilPNG         = pygame.image.load('Sprites/Alfil.png'          )
CaballoPNG       = pygame.image.load('Sprites/Caballo.png'        )
TorrePNG         = pygame.image.load('Sprites/Torre.png'          )
PeonPNG          = pygame.image.load('Sprites/Peon.png'           )
CajaPNG          = pygame.image.load('Sprites/Caja.png'           )
MenuPrincipalPNG = pygame.image.load('Sprites/MenuPrincipal.png'  )
blurPNG = [pygame.image.load('Sprites/Blur/' + str(i) +'.png') for i in range(1,11)]
#////////////////////////////////////////////////////////////////////////////////////

#Definiciones para el background
sentido = 'creciendo'
blur = 0

#Definiciones para el reloj
reloj = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

#Funcion que se usa en un loop para proveer animacion de background
def AnimacionBackground():

	#Variables globales para que no me limite la asignacion local
	global sentido
	global blur

	#Crece hasta "9" para luego devolverse
	if sentido == 'creciendo':
		 gameDisplay.blit(blurPNG[blur], (0,0))
		 blur += 1
		 if blur == 9:
		 	sentido = 'decreciendo'
	elif sentido == 'decreciendo':
		 gameDisplay.blit(blurPNG[blur], (0,0))
		 blur -= 1
		 if blur == 0:
		 	sentido = 'creciendo'	

#Loop de la Pantalla inicial del juego.
def LoopIntro():
	#Almacena el nombre de usuario
	NombreUsuario = eztext.Input(maxlength=13, color=white, prompt='Nombre de usuario: ')
	NombreUsuario.set_pos(150,350)
	Inicio = True
	while Inicio:

	#Refresca los eventos a esta variable	
		eventos = pygame.event.get()
	#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()
	#Animacion del background
		AnimacionBackground()
	#Evento para salir del juego o del loop inicial
		for event in eventos: 
			if event.type == QUIT: 
				pygame.quit() 
				sys.exit()
			if presionada[pygame.K_RETURN] and Usuario != "":
				Inicio = False
				return Usuario
	#Dibuja el input, lo actualiza y asigna a la variable 'Usuario'
		gameDisplay.blit(CajaPNG, (125,330))
		NombreUsuario.draw(gameDisplay)
		NombreUsuario.update(eventos)
		Usuario = NombreUsuario.value
	#Actualiza los dibujos de la pantalla a un determinado FPS
		pygame.display.flip()
		fpsClock.tick(FPS)

def Niveles():

	InputDificultad = eztext.Input(maxlength=1, color=white, prompt='')
	InputDificultad.set_pos(407, 422)
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)
	
	MenuNiveles = True
	while MenuNiveles:

		#Refresca los eventos a esta variable
		eventos = pygame.event.get()
		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

		AnimacionBackground()

		#CAMBIAR LAS IMAGENES
		#Cargamos las imagenes con las opciones de los diferentes niveles del juego
		gameDisplay.blit(Dificultad, (180,125))
		InputDificultad.draw(gameDisplay)
		InputDificultad.update(eventos)
		Nivel = InputDificultad.value #Guardamos el valor del inputDificultad en la variable Nivel..
		

		 #Evento para salir hacia el menu Principal o para cargar el juego en su respectivo nivel
		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()
			if presionada[pygame.K_RETURN] and Nivel == "0":
				return 
			if presionada[pygame.K_RETURN] and Nivel == "1":				
				MenuDesafio(Nivel)				
				
			if presionada[pygame.K_RETURN] and Nivel == "2":
				MenuDesafio(Nivel)
				
			if presionada[pygame.K_RETURN] and Nivel == "3":
				pass
				
			if presionada[pygame.K_RETURN] and Nivel == "4":
				pass
				

		pygame.display.update()
		fpsClock.tick(FPS)

#Se define el Loop principal del juego
def LoopPrincipal():

	gameDisplay = pygame.display.set_mode((760,760))
	#Para la escogencia de la opcion del menu, definimos un InputMenu con longitud 1 para un solo numero
	InputMenu = eztext.Input(maxlength=1, color=white, prompt='Opcion: ')
	InputMenu.set_pos(248,480)
	EzTextusuario = eztext.Input(maxlength = 0, color=white, prompt=Usuario)
	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)

	#Variable que verifica si ejecuta la parte del codigo del menu principal
	#Menunivel = Niveles()
	MenuPrincipal = True
	PantallaDeOpcionesPrincipal = True #Muestra las opciones principales
	OpcionNuevaPartida  = False        #Ejecuta el codigo de la partida nueva
	OpcionCargarPartida = False        #Ejecuta el codigo de Cargar Partida
	OpcionScoreboard    = False        #Ejecuta el codigo del Scoreboard

	#Si se cambia a True en el loop, se rompe y termina la ejecucion del juego

	while True:

	#Refresca los eventos a esta variable	
		eventos = pygame.event.get()

	#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

	#Bloque del Menu Principal
		if MenuPrincipal:

		#Animacion del background
			AnimacionBackground()

		#Muestra las Opciones principales
			if PantallaDeOpcionesPrincipal:

				gameDisplay.blit(MenuPrincipalPNG, (180,125))

				InputMenu.draw(gameDisplay)
				InputMenu.update(eventos)
				OpcionMenuPrincipal = InputMenu.value

		#Opcion Nueva Partida
			if OpcionNuevaPartida:
				OpcionNuevaPartida = False
				Niveles()
				PantallaDeOpcionesPrincipal = True
						

		#Opcion Cargar Partida
			if OpcionCargarPartida:
				###EN CONSTRUCCION### LAS TRES LINEAS DE ABAJO SON TEMPORALES
				print("Has accedido correctamente a la opcion de Cargar Partida, como esta en construccion, te retornaremos al menu principal")
				OpcionCargarPartida = False
				PantallaDeOpcionesPrincipal = True

		#Opcion Scoreboard
			if OpcionScoreboard:
				###EN CONSTRUCCION### LAS TRES LINEAS DE ABAJO SON TEMPORALES
				print("Has accedido correctamente a la opcion de scoreboard, como esta en construccion, te retornaremos al menu principal")
				OpcionScoreboard = False
				PantallaDeOpcionesPrincipal = True

	###
		###
	###		###
		###		### ESPACIO PARA EL RESTO DEL CODIGO DESHABILITANDO EL MENU PRINCIPAL
	###		###
		###
	###


	#Eventos del Loop Principal
		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()

			#Opcion de Menu para Partida Nueva
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "1":
				OpcionNuevaPartida  = True
				PantallaDeOpcionesPrincipal = False

			#Opcion de Menu para Cargar Partida
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "2":
				OpcionCargarPartida = True
				PantallaDeOpcionesPrincipal = False

			#Opcion de Menu para Scoreboard
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "3":
				OpcionScoreboard    = True
				PantallaDeOpcionesPrincipal = False

			#Opcion de Menu para salir dejuego
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "4": 
				pygame.quit() 
				sys.exit()				

	#Actualiza los dibujos de la pantalla a un determinado FPS
		pygame.display.update()
		fpsClock.tick(FPS)

			#Nivel es el parametro q determinara que opciones cargada segun el nivel

def Tablero(Nivel,PosPiezas):

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)
	
	#Variables que manejaran cuando desactivar o activar un input (Dependiendo de la opcion seleccionada)
	Mostrar_Input_Tablero_Opcion = True
	Mostrar_Input_Jugar = False
	Mostrar_Input_Jugar_0 = False
	Mostrar_Input_Jugar_1 = False
	Mostrar_Input_Pausa = False
	Mostrar_Input_Terminar = False
	#Declarar todos los inputs abajo de esto
	#---------------------------------------
	Input_Tablero_Opcion = eztext.Input(maxlength=1, color=white, prompt='Elija una opcion: ')
	Input_Tablero_Opcion.set_pos(799,720)
	Opcion_Tablero=Input_Tablero_Opcion.value
	#---------------------------------------
	Input_Jugar_0 = eztext.Input(maxlength=2, color=white, prompt='Posicion Inicial: ')
	Input_Jugar_0.set_pos(799,680)
	Jugar_0 = Input_Jugar_0.value
	#---------------------------------------
	Input_Jugar_1 = eztext.Input(maxlength=2, color=white, prompt='Posicion Final: ')
	Input_Jugar_1.set_pos(799,720)
	Jugar_1 = Input_Jugar_1.value
	#---------------------------------------
	Input_Pausa = eztext.Input(maxlength=1, color=white, prompt='Inserte 0 y presione enter para resumir: ')
	Input_Pausa.set_pos(250,350)
	Opcion_Pausa = Input_Pausa.value
	#---------------------------------------
	Input_Terminar = eztext.Input(maxlength=1, color=white, prompt='1) Salir 2) guardar: ')
	Input_Terminar.set_pos(799,680)
	Salir_o_Guardar = Input_Terminar.value
	#---------------------------------------
	#Declarar todos los inputs encima de esto

	#Ancho y largo de la ventana que se generara
	display_width  = 1060
	display_height = 760

	#Cargamos de nuevo el display del juego con los nuevos valores
	gameDisplay = pygame.display.set_mode((display_width, display_height))

	#Variables de tiempo
	TextoDeContador = 'Tiempo restante: '
	if Nivel == '1':
		contador = 3*60
	elif Nivel == '2':
		contador = int(1.5*60)

	#Nombre de usuario en pantalla
	Nombre = "Usuario: " + Usuario

	#Relativo a Deshacer
	lectura(PosPiezas)
	Deshacer_Temp_List = [MatrizToString(matriz)]
	Contador_de_deshacer = 0
	
	while True:

		#Creamos la ventana nueva y le damos nombre

		#Refresca los eventos a esta variable	
		eventos = pygame.event.get()

		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()

			#Funcion contadora de tiempo
			if event.type == pygame.USEREVENT and Mostrar_Input_Pausa == False:
				contador -= 1
				if contador > 0:
					TextoDeContador = 'Tiempo restante: ' + str(contador)
				else:
					print("Has perdido. Anadir pantalla de perder")
					return LoopPrincipal()


			#Funcion jugar
			if  Opcion_Tablero == "1" and presionada[pygame.K_RETURN]:
				Mostrar_Input_Jugar = True
				Mostrar_Input_Jugar_0 = True
				Mostrar_Input_Tablero_Opcion = False
				Input_Tablero_Opcion.value = ""

			#Relativo a Funcion Jugar: Jugar_0
			if len(Input_Jugar_0.value) == 2 and presionada[pygame.K_RETURN]:
				Mostrar_Input_Jugar_0 = False
				Mostrar_Input_Jugar_1 = True
				Pos_i = Jugar_0

			if len(Input_Jugar_1.value) == 2 and presionada[pygame.K_RETURN]:
				Pos_f = Jugar_1
				print(PosPiezas)
				Torre(Pos_i, Pos_f, matriz, PosPiezas) #PROBANDO TORRE
				Peon(Pos_i, Pos_f, matriz, PosPiezas)
				Caballo(Pos_i, Pos_f, matriz, PosPiezas)
				Jugar_0 = None
				Jugar_1 = None
				Input_Jugar_0.value = ""
				Input_Jugar_1.value = ""
				Input_Tablero_Opcion.value = ""
				Mostrar_Input_Jugar_1 = False
				Mostrar_Input_Jugar = False
				Mostrar_Input_Tablero_Opcion = True
				###### FALTAN CAMBIOS A LA MATRIZ REALMENTE Y DESPUES LO SIGUIENTE####
				lectura(PosPiezas)
				Deshacer_Temp_List.append(MatrizToString(matriz))

			#Funcion pausar
			if  Opcion_Tablero == "2" and presionada[pygame.K_RETURN]:
				Mostrar_Input_Pausa = True
				Mostrar_Input_Tablero_Opcion = False
				Opcion_Tablero = ""
				Input_Tablero_Opcion.value = ""

			#Relativo a Funcion Pausar: Resumir despues de pausar
			if Opcion_Pausa == "0" and presionada[pygame.K_RETURN]:
				Mostrar_Input_Pausa = False
				Mostrar_Input_Tablero_Opcion = True
				Opcion_Pausa = ""
				Input_Pausa.value = ""		

			#Funcion Salir
			if  Opcion_Tablero == "3" and presionada[pygame.K_RETURN]:
				Mostrar_Input_Tablero_Opcion = False
				Mostrar_Input_Terminar=True
				Opcion_Tablero = ""
				Input_Tablero_Opcion.value = ""

			#Relativo a Funcion Salir: Salir sin Guardar
			if Salir_o_Guardar == "1" and presionada[pygame.K_RETURN]:
				return LoopPrincipal()

			#Relativo a Funcion Salir: Guardar y Salir
			if Salir_o_Guardar == "2" and presionada[pygame.K_RETURN]:
				string = MatrizToString(matriz)
				lineas = sum(1 for linea in open('Texts/partidasguardadas.txt'))
				if Nivel == '1':
					strNivel = "Facil"
				elif Nivel == '2':
					strNivel = "Dificil"
				with open('Texts/partidasguardadas.txt', 'a+') as archivo:
					for lines in archivo:
						lineas += 1
					guardado = "Partida " + str(lineas + 1) + " " + time.strftime("%d/%m/%y") + " " + str(contador) + " " + strNivel + " "+ string
					print("A continuacion se guardara en una nueva linea:\n" + '"' + guardado + '"')
					archivo.write(guardado + "\n")

				return LoopPrincipal()

			#Funcion Deshacer
			if  Opcion_Tablero == "4" and presionada[pygame.K_RETURN] and Nivel == "1":
				Opcion_Tablero = ""
				Input_Tablero_Opcion.value = ""
				if len(Deshacer_Temp_List) - Contador_de_deshacer > 1:
					Contador_de_deshacer += 1
					PosPiezas = Deshacer_Temp_List[len(Deshacer_Temp_List) - Contador_de_deshacer - 1].split('-')
					lectura(PosPiezas)
					print("Antes) indice: " + str(len(Deshacer_Temp_List) - 1) + " string: " + Deshacer_Temp_List[len(Deshacer_Temp_List) - 1])
					print("Ahora) indice: " + str(len(Deshacer_Temp_List) - Contador_de_deshacer - 1) + " string: " + Deshacer_Temp_List[len(Deshacer_Temp_List) - Contador_de_deshacer - 1])
				else:
					print("ERROR, has deshecho todo lo posible, esta es la lista temporal actual:" + str(Deshacer_Temp_List))


		#En caso de ser nivel 1(Facil) cargara el menu con botones faciles
		if Nivel == "1":
			gameDisplay.blit(Opcionesfacil,(758,0))
		#En caso de ser nivel 2(dificil) cargara el menu con los botones dificiles
		elif Nivel == "2":
			gameDisplay.blit(OpcionesDificil,(758,0))

		gameDisplay.blit(TableroPNG,(0,0))

		if Mostrar_Input_Tablero_Opcion == True:
			Input_Tablero_Opcion.draw(gameDisplay)
			Input_Tablero_Opcion.update(eventos)			
			Opcion_Tablero=Input_Tablero_Opcion.value

		if Mostrar_Input_Jugar == True:
			Input_Jugar_0.draw(gameDisplay)
			Input_Jugar_1.draw(gameDisplay)

			if Mostrar_Input_Jugar_0 == True:
				Input_Jugar_0.draw(gameDisplay)				
				Input_Jugar_0.update(eventos)
				Jugar_0 = Input_Jugar_0.value
			
			if Mostrar_Input_Jugar_1 == True:
				Input_Jugar_1.draw(gameDisplay)				
				Input_Jugar_1.update(eventos)
				Jugar_1 = Input_Jugar_1.value


		if Mostrar_Input_Terminar == True:
			Input_Terminar.draw(gameDisplay)
			Input_Terminar.update(eventos)
			Salir_o_Guardar = Input_Terminar.value	


		gameDisplay.blit(TableroPNG,(0,0))

		lectura(PosPiezas)




		#Pantalla de Pausa
		if Mostrar_Input_Pausa == True:
			gameDisplay.blit(TableroPNG,(0,0))
			gameDisplay.blit(CajaPNG, (250, 350))
			Input_Pausa.draw(gameDisplay)
			Input_Pausa.update(eventos)
			Opcion_Pausa = Input_Pausa.value

		#Pantalla de Tiempo
		gameDisplay.blit(Font.render(TextoDeContador, True, black), (5,5))

		#Pantalla de Nombre
		gameDisplay.blit(Font.render(Nombre, True, black), (5, 30))

		pygame.display.update()
		fpsClock.tick(FPS)

				#OpcionMenuNiveles es el parametro que guarda el nivel(facil/dif...)

def MenuDesafio(Nivel):

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)

	InputCargado = eztext.Input(maxlength=1, color=white, prompt='')
	InputCargado.set_pos(495, 263)

	while True:
		#Refresca los eventos a esta variable	
		eventos = pygame.event.get()

		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

		#Animacion del background
		AnimacionBackground()

		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()


			if presionada[pygame.K_RETURN] and Opcion_Teclado_Desafio == "1":
				#Llamamos la funcion que contiene la ventana del input para el usuario cree su tablero
				Configuracion_por_teclado(Nivel)


		gameDisplay.blit(CargadoTablero,(198,90))
		gameDisplay.blit(DesafioTeclado,(90,350))
		InputCargado.draw(gameDisplay)
		
		InputCargado.update(eventos)
		Opcion_Teclado_Desafio= InputCargado.value
		pygame.display.update()
		fpsClock.tick(FPS)

def lectura(PosPiezas):
	global matriz
	matriz = {
			  1:{'a':0, 'b':0, 'c':0, 'd':0},
			  2:{'a':0, 'b':0, 'c':0, 'd':0},
			  3:{'a':0, 'b':0, 'c':0, 'd':0},
			  4:{'a':0, 'b':0, 'c':0, 'd':0}
			 }
	x=0
	y=0

	for pieza in PosPiezas:
		if len(pieza) == 3:

			if pieza[0].lower() == "t":
				if pieza[1]=="a":
					matriz[int(pieza[2])]['a']="t"
					x=69
				elif pieza[1] == "b":
					matriz[int(pieza[2])]['b']="t"
					x=225
				elif pieza[1] == "c":
					matriz[int(pieza[2])]['c']="t"
					x=381
				elif pieza[1] == "d":
					matriz[int(pieza[2])]['d']="t"
					x=538

				if pieza[2]=="4":
					gameDisplay.blit(TorrePNG, (x,65)) 

				elif pieza[2]=="3":
					gameDisplay.blit(TorrePNG, (x,222)) 

				elif pieza[2] == "2":
					gameDisplay.blit(TorrePNG, (x,378)) 

				elif pieza[2] == "1":
					gameDisplay.blit(TorrePNG, (x,536)) 

			elif pieza[0].lower() == "c":
				if pieza[1]=="a":
					matriz[int(pieza[2])]['a']="c"
					x=69
				elif pieza[1] == "b":
					matriz[int(pieza[2])]['b']="c"
					x=225
				elif pieza[1] == "c":
					matriz[int(pieza[2])]['c']="c"
					x=381
				elif pieza[1] == "d":
					matriz[int(pieza[2])]['d']="c"
					x=538

				if pieza[2]=="4":
					gameDisplay.blit(CaballoPNG, (x,65)) 

				elif pieza[2]=="3":
					gameDisplay.blit(CaballoPNG, (x,222)) 

				elif pieza[2] == "2":
					gameDisplay.blit(CaballoPNG, (x,378)) 

				elif pieza[2] == "1":
					gameDisplay.blit(CaballoPNG, (x,534)) 

			elif pieza[0].lower() == "a":
				if pieza[1]=="a":
					matriz[int(pieza[2])]['a']="a"
					x=69
				elif pieza[1] == "b":
					matriz[int(pieza[2])]['b']="a"
					x=225
				elif pieza[1] == "c":
					matriz[int(pieza[2])]['c']="a"
					x=381
				elif pieza[1] == "d":
					matriz[int(pieza[2])]['d']="a"
					x=538

				if pieza[2]=="4":
					gameDisplay.blit(AlfilPNG, (x,65)) 

				elif pieza[2]=="3":
					gameDisplay.blit(AlfilPNG, (x,222)) 

				elif pieza[2] == "2":
					gameDisplay.blit(AlfilPNG, (x,378)) 

				elif pieza[2] == "1":
					gameDisplay.blit(AlfilPNG, (x,534)) 

			elif pieza[0].lower() == "r":
				if pieza[1]=="a":
					matriz[int(pieza[2])]['a']="r"
					x=69
				elif pieza[1] == "b":
					matriz[int(pieza[2])]['b']="r"
					x=225
				elif pieza[1] == "c":
					matriz[int(pieza[2])]['c']="r"
					x=381
				elif pieza[1] == "d":
					matriz[int(pieza[2])]['d']="r"
					x=538

				if pieza[2]=="4":
					gameDisplay.blit(ReyPNG, (x,65)) 

				elif pieza[2]=="3":
					gameDisplay.blit(ReyPNG, (x,222)) 

				elif pieza[2] == "2":
					gameDisplay.blit(ReyPNG, (x,378)) 

				elif pieza[2] == "1":
					gameDisplay.blit(ReyPNG, (x,534)) 

			elif pieza[0].lower() == "d":
				if pieza[1]=="a":
					matriz[int(pieza[2])]['a']="d"
					x=69
				elif pieza[1] == "b":
					matriz[int(pieza[2])]['b']="d"
					x=225
				elif pieza[1] == "c":
					matriz[int(pieza[2])]['c']="d"
					x=381
				elif pieza[1] == "d":
					matriz[int(pieza[2])]['d']="d"
					x=538

				if pieza[2]=="4":
					gameDisplay.blit(DamaPNG, (x,65)) 

				elif pieza[2]=="3":
					gameDisplay.blit(DamaPNG, (x,222)) 

				elif pieza[2] == "2":
					gameDisplay.blit(DamaPNG, (x,378)) 

				elif pieza[2] == "1":
					gameDisplay.blit(DamaPNG, (x,534)) 

		elif len(pieza)==2:
				if pieza[0]=="a":
					matriz[int(pieza[1])]['a']="P"
					x=69
				elif pieza[0] == "b":
					matriz[int(pieza[1])]['b']="P"
					x=225
				elif pieza[0] == "c":
					matriz[int(pieza[1])]['c']="P"
					x=381
				elif pieza[0] == "d":
					matriz[int(pieza[1])]['d']="P"
					x=538

				if pieza[1]=="4":
					gameDisplay.blit(PeonPNG, (x,65)) 

				elif pieza[1]=="3":
					gameDisplay.blit(PeonPNG, (x,222)) 

				elif pieza[1] == "2":
					gameDisplay.blit(PeonPNG, (x,378)) 

				elif pieza[1] == "1":
					gameDisplay.blit(PeonPNG, (x,534))

	return matriz

def MatrizToString(Matriz):
	string = ""
	tmp = []
	for i, j in Matriz.items(): #i = key, j = value del diccionario Matriz
		for k, v in j.items(): # k = key, v = value de los diccionarios que son cada j
			if v == 'P': #Si v es un peon
				tmp.append(str(k) + str(i)) #No se anade la P
			elif v != 0: #Si no esta vacio, se anade el valor
				tmp.append(str(v).upper() + str(k) + str(i))

	for i in range(len(tmp)):
		if i == 0:
			string += tmp[i]
		else:
			string += '-' + tmp[i]

	print(string)
	return string

def Configuracion_por_teclado(Nivel):

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)

	#Cargara la cuadricula para habilitarle al usuario el poder ingresar como desea el tablero
	InputConfiguracionTeclado = eztext.Input(maxlength=31, color=white, prompt='Introduce tu configuracion: ')
	InputConfiguracionTeclado.set_pos(0,727)
	InputConfiguracionTeclado.value="ta1-ca2-ra3-da4-ad1-td2-ad3-cc3" #METODO PARA PROBAR LA POSICION DE LAS FICHAS

	while True:

		eventos = pygame.event.get()

		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

		#Efecto de animacion
		AnimacionBackground()

		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()

			if presionada[pygame.K_RETURN]: #colocar la condicion de que sea un string valido
				#Convertimos el string de configuracion_Teclado en una lista
				InputConfiguracionTeclado.value = InputConfiguracionTeclado.value.split('-')
				PosPieza = InputConfiguracionTeclado.value
				PosPiezas = []
				for elemento in PosPieza:
					if len(elemento) == 2:
						print("len 2")
						PosPiezas.append(elemento.lower())
					elif len(elemento) == 3:
						print("len 3")
						PosPiezas.append(elemento[0].upper() + elemento[1:].lower())
						print(elemento)
				print(PosPiezas)
				#retornamos el tablero con el nivel seleccionado
				Tablero(Nivel,PosPiezas)


		gameDisplay.blit(CajaPNG,(0,717))
		gameDisplay.blit(CajaPNG,(300,717))
		gameDisplay.blit(CajaPNG,(600,717))
		gameDisplay.blit(Leyenda,(88,145))
		InputConfiguracionTeclado.draw(gameDisplay)
		InputConfiguracionTeclado.update(eventos)
		#Asignamos el valor de la configuracion a la variable Configuracion_teclado
		Configuracion_Teclado = InputConfiguracionTeclado.value
		pygame.display.update()
		fpsClock.tick(FPS)

def Torre(Pos_i, Pos_f, Matriz, PosPiezas):
	try:
		Pos_i = [Pos_i[:1], int(Pos_i[1:])] #letra, numero
		Pos_f = [Pos_f[:1], int(Pos_f[1:])] #letra, numero
		posibles = [] #lista de posibles jugadas, cada elemento sera [letra, numero], numero en int
		posiblesRef = [] #lista refinada de "posibles"
		assert(Matriz[Pos_i[1]][Pos_i[0]].lower() == "t" and Matriz[Pos_f[1]][Pos_f[0]] != 0) #que el inicial sea torre y el final distinto de 0

		#En este for, se construye la lista de posibles para la torre, sin refinar.
		for numero, diccionario in Matriz.items():
			for letra, pieza in diccionario.items():			
				if numero == Pos_i[1]: #Primero trabajamos en el eje de los numeros
					if pieza != 0 and letra != Pos_i[0]: #Si hay una pieza				
						posibles.append([letra, numero])
				if letra == Pos_i[0]: #Ahora trabajamos en el eje de las letras
					if pieza != 0 and numero != Pos_i[1]: #Si hay una pieza
						posibles.append([letra, numero])

		#Variables usadas para refinar la lista de posibles jugadas
		tmp_letra_mayor = 'z'
		tmp_letra_menor = '1'
		tmp_numero_mayor = 10
		tmp_numero_menor = 0
		TMPNumLETRA =    "No"
		tmpNumletra =    "No"
		tmpLetraNUMERO = "No"
		tmpLetranumero = "No"

		#Refinando la lista
		for valor in posibles:

			if valor[1] == Pos_i[1]: #Mismo numero
				if valor[0] > Pos_i[0]: #letra mayor a la inicial
					if valor[0] < tmp_letra_mayor: #El valor actual", valor[0], "es menor que la tmp actual", tmp_letra_mayor
						tmp_letra_mayor = valor[0]
						TMPNumLETRA = valor
				elif valor[0] < Pos_i[0]: #letra menor a la inicial
					if valor[0] > tmp_letra_menor:
						tmp_letra_menor = valor[0]
						tmpNumletra = valor

			elif valor[0] == Pos_i[0]: #Misma letra
				if valor[1] > Pos_i[1]: #
					if valor[1] < tmp_numero_mayor: #El valor actual", valor[1], "es menor que la tmp actual", tmp_numero_mayor
						tmp_numero_mayor = valor[1]
						tmpLetraNUMERO = valor			
				elif valor[1] < Pos_i[1]: #numero menor al inicial
					if valor[1] > tmp_numero_menor:
						tmp_numero_menor = valor[1]
						tmpLetranumero = valor				

		#anadiendo a posiblesRef
		if TMPNumLETRA !=    "No":
			posiblesRef.append(TMPNumLETRA)
		if tmpNumletra !=    "No":
			posiblesRef.append(tmpNumletra)
		if tmpLetraNUMERO != "No":
			posiblesRef.append(tmpLetraNUMERO)
		if tmpLetranumero != "No":
			posiblesRef.append(tmpLetranumero)

		print(posiblesRef)
		print(PosPiezas)
		#En este for se busca la posicion final entre los posibles y se cambia el inicial por "0" y el final por la torre
		try:
			PosPiezas.remove((Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('R' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('D' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('A' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('C' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('T' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass			

		PosPiezas.remove("T" + (Pos_i[0] + str(Pos_i[1])).lower())

		for posible in posiblesRef:
			if posible[0] == Pos_f[0] and posible[1] == Pos_f[1]:
				PosPiezas.append("T" + Pos_f[0] + str(Pos_f[1]))
		print(PosPiezas)
		return PosPiezas	

	except:
		print("La pieza inicial no es una Torre, o algo peor ha sucedido")

def CambioLetra(letra, sentido):
	if sentido == 1:
		if letra == 'a':
			return 'b'
		elif letra == 'b':
			return 'c'
		elif letra == 'c':
			return 'd'
		elif letra == 'd':
			return False
	elif sentido == -1:
		if letra == 'a':
			return False
		elif letra == 'b':
			return 'a'
		elif letra == 'c':
			return 'b'
		elif letra == 'd':
			return 'c'	
	elif sentido == 2:
		if letra == 'a':
			return 'c'
		elif letra == 'b':
			return 'd'
		elif letra == 'c':
			return False
		elif letra == 'd':
			return False		
	elif sentido == -2:	
		if letra == 'a':
			return False
		elif letra == 'b':
			return False
		elif letra == 'c':
			return 'a'
		elif letra == 'd':
			return 'b'

def Peon(Pos_i, Pos_f, Matriz, PosPiezas):

	try:
		Pos_i = [Pos_i[:1], int(Pos_i[1:])] #letra, numero
		Pos_f = [Pos_f[:1], int(Pos_f[1:])] #letra, numero
		posibles = [] #lista de posibles jugadas, cada elemento sera [letra, numero], numero en int
		assert(Matriz[Pos_i[1]][Pos_i[0]].lower() == "p" and Matriz[Pos_f[1]][Pos_f[0]] != 0) #que el inicial sea torre y el final distinto de 0
		#En este for, se construye la lista de posibles para el peon, sin refinar.
		for numero, diccionario in Matriz.items():
			for letra, pieza in diccionario.items():
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 1) and numero == Pos_i[1] + 1:
					posibles.append([letra, numero])		
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -1) and numero == Pos_i[1] + 1:
					posibles.append([letra, numero])
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -1) and numero == Pos_i[1] - 1:
					posibles.append([letra, numero])	
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 1) and numero == Pos_i[1] - 1:
					posibles.append([letra, numero])	
		
		print(posibles)

		try:
			PosPiezas.remove((Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('R' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('D' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('A' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('C' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('T' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass			

		PosPiezas.remove((Pos_i[0] + str(Pos_i[1])).lower())

		for posible in posibles:
			if posible[0] == Pos_f[0] and posible[1] == Pos_f[1]:
				PosPiezas.append(Pos_f[0] + str(Pos_f[1]))
		print(PosPiezas)
		return PosPiezas	


	except:
		print("La pieza inicial no es un Peon, o algo peor ha sucedido")

def Caballo(Pos_i, Pos_f, Matriz, PosPiezas):
	try:
		Pos_i = [Pos_i[:1], int(Pos_i[1:])] #letra, numero
		Pos_f = [Pos_f[:1], int(Pos_f[1:])] #letra, numero
		posibles = [] #lista de posibles jugadas, cada elemento sera [letra, numero], numero en int
		assert(Matriz[Pos_i[1]][Pos_i[0]].lower() == "c" and Matriz[Pos_f[1]][Pos_f[0]] != 0) #que el inicial sea torre y el final distinto de 0
		#En este for, se construye la lista de posibles para el peon, sin refinar.
		for numero, diccionario in Matriz.items():
			for letra, pieza in diccionario.items():
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 2) and numero == Pos_i[1] + 1:
					posibles.append([letra, numero])		
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 1) and numero == Pos_i[1] + 2:
					posibles.append([letra, numero])
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -1) and numero == Pos_i[1] + 2:
					posibles.append([letra, numero])	
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -2) and numero == Pos_i[1] + 1:
					posibles.append([letra, numero])	
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -2) and numero == Pos_i[1] - 1:
					posibles.append([letra, numero])		
				if pieza != 0 and letra == CambioLetra(Pos_i[0], -1) and numero == Pos_i[1] - 2:
					posibles.append([letra, numero])
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 1) and numero == Pos_i[1] - 2:
					posibles.append([letra, numero])	
				if pieza != 0 and letra == CambioLetra(Pos_i[0], 2) and numero == Pos_i[1] - 1:
					posibles.append([letra, numero])

		print(posibles)

		try:
			PosPiezas.remove((Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('R' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('D' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:
			PosPiezas.remove('A' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('C' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass
		try:			
			PosPiezas.remove('T' + (Pos_f[0] + str(Pos_f[1])).lower())
		except:
			pass		

		PosPiezas.remove(("C" + Pos_i[0] + str(Pos_i[1])).lower())

		for posible in posibles:
			if posible[0] == Pos_f[0] and posible[1] == Pos_f[1]:
				PosPiezas.append("C" + Pos_f[0] + str(Pos_f[1]))

		print(PosPiezas)
		return PosPiezas	


	except:
		print("La pieza inicial no es un Caballo, o algo peor ha sucedido")




#Se asigna a la variable Usuario el nombre del usuario

global Usuario
Usuario = LoopIntro()

#Se ejecuta el loop principal que contiene al menu y demas cosas
LoopPrincipal()