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
TableroPNG = pygame.image.load('Sprites/tablero.png')
ReyPNG     = pygame.image.load('Sprites/Rey.png'    )
ReinaPNG   = pygame.image.load('Sprites/Reina.png'  )
AlfilPNG   = pygame.image.load('Sprites/Alfil.png'  )
CaballoPNG = pygame.image.load('Sprites/Caballo.png')
TorrePNG   = pygame.image.load('Sprites/Torre.png'  )
PeonPNG    = pygame.image.load('Sprites/Peon.png'   )
CajaPNG    = pygame.image.load('Sprites/Caja.png'   )
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

#Se asigna a la variable Usuario el nombre del usuario
Usuario = LoopIntro()

#Se define el Loop principal del juego
def LoopPrincipal():

	MenuPrincipal = True
	
	while True:
		if MenuPrincipal:
			ffwe
		#Ejecutar Pantalla Principal con BGintro True con opciones partida nueva,
		# cargar partida, tabla de records, salir del juego 
		#(referencia http://i.imgur.com/CfA3ZAQ.png ) 

		#Evento para salir del juego
			for event in pygame.event.get(): 
				if event.type == pygame.locals.QUIT: 
					pygame.quit() 
					sys.exit()

		#Actualiza los dibujos de la pantalla a un determinado FPS
			pygame.display.update()
			fpsClock.tick(FPS)


