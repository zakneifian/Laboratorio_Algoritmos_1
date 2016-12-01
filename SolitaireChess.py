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
CargadoTablero 	 = pygame.image.load('Sprites/CargadoTablero.png')
Cartadesafio	 = pygame.image.load('Sprites/Cartadesafio.png'	)
Cargarteclado 	 = pygame.image.load('Sprites/Cargarteclado.png')
Opcionesfacil 	 = pygame.image.load('Sprites/OpcionesFacil.png')
Opciondificil	 = pygame.image.load('Sprites/Dificil.png'      )
regresar 		 = pygame.image.load('Sprites/regresar.png'		)
Leyenda			 = pygame.image.load('Sprites/Leyenda.png'		)
MensajeLeyenda   = pygame.image.load('Sprites/Mensaje1.png'		)
tutorial 		 = pygame.image.load('Sprites/tutorial.png'		)
facil 			 = pygame.image.load('Sprites/facil.png'   		)
dificil 		 = pygame.image.load('Sprites/dificil.png' 		)
muydificil 		 = pygame.image.load('Sprites/muydificil.png'  	)
TableroPNG       = pygame.image.load('Sprites/Tablero.png'      )
ReyPNG           = pygame.image.load('Sprites/Rey.png'          )
ReinaPNG         = pygame.image.load('Sprites/Reina.png'        )
AlfilPNG         = pygame.image.load('Sprites/Alfil.png'        )
CaballoPNG       = pygame.image.load('Sprites/Caballo.png'      )
TorrePNG         = pygame.image.load('Sprites/Torre.png'        )
PeonPNG          = pygame.image.load('Sprites/Peon.png'         )
CajaPNG          = pygame.image.load('Sprites/Caja.png'         )
MenuPrincipalPNG = pygame.image.load('Sprites/MenuPrincipal.png')
blurPNG = [pygame.image.load('Sprites/Blur/' + str(i) +'.png') for i in range(1,11)]
#////////////////////////////////////////////////////////////////////////////////////

#Definiciones para el background
sentido = 'creciendo'
blur = 0

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

	InputDificultad = eztext.Input(maxlength=1, color=white, prompt='Elija el nivel de dificultad: ')
	InputDificultad.set_pos(250, 380)
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)
	#PROBANDO TRABAJAR CON MIDDLE DE LOS IMGS
	#self.rect = self.EzTextusuario.get_rect()
	#self.EzTextusuario.rect.centery = 10
	#self.EzTextusuario.rect.centerx = display_width/2

	MenuNiveles = True
	while MenuNiveles:

		#Refresca los eventos a esta variable
		eventos = pygame.event.get()
		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

		AnimacionBackground()

		#CAMBIAR LAS IMAGENES
		#Cargamos las imagenes con las opciones de los diferentes niveles del juego
		gameDisplay.blit(regresar, (340,580))
		gameDisplay.blit(CajaPNG, (155,370))
		gameDisplay.blit(facil, (120,120))
		gameDisplay.blit(dificil, (580,120))
		gameDisplay.blit(muydificil, (120,580))
		gameDisplay.blit(tutorial, (580,580))
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
	SalirDelJuego = False

	while not SalirDelJuego:

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
				SalirDelJuego       = True

	#Actualiza los dibujos de la pantalla a un determinado FPS
		pygame.display.update()
		fpsClock.tick(FPS)

			#Nivel es el parametro q determinara que opciones cargada segun el nivel
def Tablero(Nivel):

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)
	
	#Variables que manejaran cuando desactivar o activar un input (Dependiendo de la opcion seleccionada)
	Valor_Terminar=False
	Valor_Terminar2=True
	#Activa el input para seleccionar una de las opciones (jugar, pausar, terminar etc)
	if Valor_Terminar2 == True:
		Input_Tablero_Opcion = eztext.Input(maxlength=1, color=white, prompt='Elija una opcion: ')
		Input_Tablero_Opcion.set_pos(799,720)
		Opcion_Tablero=Input_Tablero_Opcion.value

	Input_Terminar = eztext.Input(maxlength=0, color=white, prompt='1) Salir 2) guardar: ')
	Input_Terminar.set_pos(799,680)
	Salir_o_Guardar = Input_Terminar.value

	#Ancho y largo de la ventana que se generara
	display_width  = 1060
	display_height = 760

	#Cargamos de nuevo el display del juego con los nuevos valores
	gameDisplay = pygame.display.set_mode((display_width, display_height))
	
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
			#Si selecciona terminar, desactivara la variable que permite el input de opciones y abrira el input de guardar o salir
			if  Opcion_Tablero == "3" and presionada[pygame.K_RETURN]:
				Valor_Terminar=True
				Valor_Terminar2=False
				Input_Terminar = eztext.Input(maxlength=1, color=white, prompt='1) Salir 2) guardar: ')
				Input_Terminar.set_pos(799,680)
				Salir_o_Guardar = Input_Terminar.value
				Opcion_Tablero="0"
			#Retornamos al menu principal en caso de que su seleccion sea Salir del juego
			if Salir_o_Guardar == "1" and presionada[pygame.K_RETURN]:
				display_width=760
				display_height=760
				gameDisplay = pygame.display.set_mode((display_width, display_height))
				return LoopPrincipal()

		#En caso de ser nivel 1(Facil) cargara el menu con botones faciles
		if Nivel == "1":
			gameDisplay.blit(Opcionesfacil,(758,0))
		#En caso de ser nivel 2(dificil) cargara el menu con los botones dificiles
		elif Nivel == "2":
			gameDisplay.blit(Opciondificil,(758,0))

		gameDisplay.blit(TableroPNG,(0,0))
		if Valor_Terminar==True:
			Input_Terminar.draw(gameDisplay)
			Input_Terminar.update(eventos)
		if Valor_Terminar2==True:
			Input_Tablero_Opcion.draw(gameDisplay)
			Input_Tablero_Opcion.update(eventos)	
		Opcion_Tablero=Input_Tablero_Opcion.value
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
		gameDisplay.blit(Cargarteclado,(0,100))
		gameDisplay.blit(Cartadesafio,(600,100))
		InputCargado.draw(gameDisplay)
		
		InputCargado.update(eventos)
		Opcion_Teclado_Desafio= InputCargado.value
		pygame.display.update()
		fpsClock.tick(FPS)

def Configuracion_por_teclado(Nivel):

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)

	#Cargara la cuadricula para habilitarle al usuario el poder ingresar como desea el tablero
	InputConfiguracionTeclado = eztext.Input(maxlength=40, color=white, prompt='Introduce tu configuracion: ')
	InputConfiguracionTeclado.set_pos(0,380)

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
				Configuracion_Teclado = Configuracion_Teclado.split('-')
				#retornamos el tablero con el nivel seleccionado
				Tablero(Nivel)


		gameDisplay.blit(CajaPNG,(0,367))
		gameDisplay.blit(CajaPNG,(300,367))
		gameDisplay.blit(CajaPNG,(600,367))
		gameDisplay.blit(Leyenda,(150,0))
		gameDisplay.blit(MensajeLeyenda, (150,440))
		InputConfiguracionTeclado.draw(gameDisplay)
		InputConfiguracionTeclado.update(eventos)
		#Asignamos el valor de la configuracion a la variable Configuracion_teclado
		Configuracion_Teclado = InputConfiguracionTeclado.value
		pygame.display.update()
		fpsClock.tick(FPS)

#Se asigna a la variable Usuario el nombre del usuario
Usuario = LoopIntro()

#Se ejecuta el loop principal que contiene al menu y demas cosas
LoopPrincipal()