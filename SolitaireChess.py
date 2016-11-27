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
			if presionada[pygame.K_RETURN]:
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


#Se define el Loop principal del juego
def LoopPrincipal():

	#Para la escogencia de la opcion del menu, definimos un InputMenu con longitud 1 para un solo numero
	InputMenu = eztext.Input(maxlength=1, color=black, prompt='Opcion: ')
	InputMenu.set_pos(150,440)
	#Variables del background
	sentido = 'creciendo'
	blur = 0

	#Variable que verifica si ejecuta la parte del codigo del menu principal
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
				gameDisplay.blit(MenuPrincipalPNG, (125,125)) #NOTA: Cambiar MenuPrincipalPNG

			#Hacemos blit del InputMenu sobre algun espacio inferior de MenuPrincipalPNG
				InputMenu.draw(gameDisplay)
				InputMenu.update(eventos)
				OpcionMenuPrincipal = InputMenu.value
			#(referencia http://i.imgur.com/CfA3ZAQ.png ) 

		#Opcion Nueva Partida
			if OpcionNuevaPartida:
				###EN CONSTRUCCION### LAS TRES LINEAS DE ABAJO SON TEMPORALES
				print("Has accedido correctamente a la opcion de Nueva Partida, como esta en construccion, te retornaremos al menu principal")
				OpcionNuevaPartida = False
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






#Se asigna a la variable Usuario el nombre del usuario
Usuario = LoopIntro()

#Se ejecuta el loop principal que contiene al menu y demas cosas
LoopPrincipal()