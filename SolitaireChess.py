#Recomendacion: Para lectura mas simple del archivo, cerrar pestanas de comentarios, cerrando codigo

#Librerias a importar
import pygame
from pygame.locals import *
import time
import random
import sys
import eztext

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
regresar 		 = pygame.image.load('Sprites/regresar.png'		)
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

#Loop de la Pantalla inicial del juego.
def LoopIntro():
	#Con EzText, crea el input y lo posiciona en 150, 350, maximo length de 13 por la caja en la que aparece
	NombreUsuario = eztext.Input(maxlength=13, color=white, prompt='Nombre de usuario: ')
	NombreUsuario.set_pos(150,350)

	#Variables del background
	sentido = 'creciendo'
	blur = 0

	#Variable que mantiene el loop activo
	Inicio = True

	#Loop del Intro
	while Inicio:

	#Refresca los eventos a esta variable	
		eventos = pygame.event.get()

	#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()

	#Animacion del background
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
		pass


def Niveles():
	InputDificultad = eztext.Input(maxlength=1, color=white, prompt='Elija el nivel de dificultad: ')
	InputDificultad.set_pos(250, 380)
	EzTextusuario = eztext.Input(maxlength=0, color=white, prompt=Usuario)
	EzTextusuario.set_pos(330,10)
	#PROBANDO TRABAJAR CON MIDDLE DE LOS IMGS
	#self.rect = self.EzTextusuario.get_rect()
	#self.EzTextusuario.rect.centery = 10
	#self.EzTextusuario.rect.centerx = display_width/2
	#Variables del background
	sentido = 'creciendo'
	blur = 0

	MenuNiveles = True
	MenuPrincipal = True

	while MenuNiveles:
		#Refresca los eventos a esta variable
		eventos = pygame.event.get()
		pass
		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()
		pass

		if MenuPrincipal:
		#Animacion del background
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


		if MenuNiveles: #pantallaniveles
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
			EzTextusuario.draw(gameDisplay)
			OpcionMenuNiveles = InputDificultad.value #Guardamos el valor del inputDificultad en la variable OpcionMenuNiveles..
			pygame.display.flip()
			pygame.display.update()
			fpsClock.tick(FPS)
		 	#Evento para salir hacia el menu Principal o para cargar el juego en su respectivo nivel
		for event in eventos:

			if event.type == pygame.locals.QUIT: 
				pygame.quit() 
				sys.exit()
			if presionada[pygame.K_RETURN] and OpcionMenuNiveles == "0":
				return 
			if presionada[pygame.K_RETURN] and OpcionMenuNiveles == "1":
				Tablero(OpcionMenuNiveles)
				pass
				#return FUNCION_JUEGO_FACIL()
			if presionada[pygame.K_RETURN] and OpcionMenuNiveles == "2":
				pass
				#return FUNCION_JUEGO_DIFICIL()
			if presionada[pygame.K_RETURN] and OpcionMenuNiveles == "3":
				pass
				#return FUNCION_JUEGO_MUYDIFICIL()
			if presionada[pygame.K_RETURN] and OpcionMenuNiveles == "4":
				pass
				#return FUNCION_JUEGO_TUTORIAL()

#Se define el Loop principal del juego
def LoopPrincipal():

	#Para la escogencia de la opcion del menu, definimos un InputMenu con longitud 1 para un solo numero
	InputMenu = eztext.Input(maxlength=1, color=black, prompt='Opcion: ')
	InputMenu.set_pos(180,440)

	#Muesta el nombre del usuario que esta jugando
	EzTextusuario = eztext.Input(maxlength=0, color=white, prompt=Usuario)
	EzTextusuario.set_pos(330,10)

	#Variables del background
	sentido = 'creciendo'
	blur = 0

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
		pass

	#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()
		pass

	#Bloque del Menu Principal
		if MenuPrincipal:

		#Animacion del background
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

		#Muestra las Opciones principales
			if PantallaDeOpcionesPrincipal:
			#Hacer blit del menu como tal
				gameDisplay.blit(MenuPrincipalPNG, (180,125)) #NOTA: Cambiar MenuPrincipalPNG

			#Hacemos blit del InputMenu sobre algun espacio inferior de MenuPrincipalPNG
				InputMenu.draw(gameDisplay)
				InputMenu.update(eventos)
				EzTextusuario.draw(gameDisplay)
				OpcionMenuPrincipal = InputMenu.value
			#(referencia http://i.imgur.com/CfA3ZAQ.png ) 
#----------------------------
		#Opcion Nueva Partida
#----------------------------
			if OpcionNuevaPartida:
				###EN CONSTRUCCION### LAS TRES LINEAS DE ABAJO SON TEMPORALES
				print("Has accedido correctamente a la opcion de Nueva Partida, como esta en construccion, te retornaremos al menu principal")
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
				OpcionMenuPrincipal = ""

			#Opcion de Menu para Cargar Partida
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "2":
				OpcionCargarPartida = True
				PantallaDeOpcionesPrincipal = False
				OpcionMenuPrincipal = ""

			#Opcion de Menu para Scoreboard
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "3":
				OpcionScoreboard    = True
				PantallaDeOpcionesPrincipal = False
				OpcionMenuPrincipal = ""

			#Opcion de Menu para salir dejuego
			if presionada[pygame.K_RETURN] and OpcionMenuPrincipal == "4": 
				SalirDelJuego       = True

	#Actualiza los dibujos de la pantalla a un determinado FPS
		pygame.display.update()
		fpsClock.tick(FPS)

def Tablero(OpcionMenuNiveles):

	while True:
		#Ancho y largo de la ventana que se generara
		display_width  = 1060
		display_height = 760

		#Creamos la ventana y le damos nombre
		gameDisplay = pygame.display.set_mode((display_width, display_height))
		gameDisplay.blit(TableroPNG,(0,0))
		pygame.display.flip()
		pygame.display.update()

		#Refresca los eventos a esta variable
		eventos = pygame.event.get()
		pass
		#Variable que verifica si una tecla esta presionada
		presionada = pygame.key.get_pressed()
		pass
		if OpcionMenuNiveles == "1":
			pass







#Se asigna a la variable Usuario el nombre del usuario
Usuario = LoopIntro()

#Se ejecuta el loop principal que contiene al menu y demas cosas
LoopPrincipal()