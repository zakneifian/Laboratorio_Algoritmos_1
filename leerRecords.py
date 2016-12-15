def LeerRecords():

	#Muesta el nombre del usuario que esta jugando en la ventana
	pygame.display.set_caption('USB\'s Solitaire Chess - ' + Usuario)

	with open("Texts/records.txt", "r") as archivo:
		contenido = archivo.readlines()
		print(contenido)
		contador=0
		condicion4=False
		condicion5=False
		condicion6=False
		condicion7=False
		y = 0
		input1 = eztext.Input(maxlength = 0, prompt='')
		input2 = eztext.Input(maxlength = 0, prompt='')
		input3 = eztext.Input(maxlength = 0, prompt='')
		input4 = eztext.Input(maxlength = 0, prompt='')
		input5 = eztext.Input(maxlength = 0, prompt='')
		input6 = eztext.Input(maxlength = 0, prompt='')
		input7 = eztext.Input(maxlength = 0, prompt='')
		input8 = eztext.Input(maxlength = 0, prompt='')
		numrecords = len(contenido)
		lista=[0,1,2,3,4,5,6,7]
		for i in range(numrecords):
			if i == 0:
				condicion0=True
				lista[i]=input1
			elif i == 1:
				condicion1=True
				lista[i]=input2
			elif i == 2:
				condicion2=True
				lista[i]=input3
			elif i == 3:
				condicion3=True
				lista[i]=input4
			elif i == 4:
				condicion4=True
				lista[i]=input5
			elif i == 5:
				condicion5=True
				lista[i]=input6
			elif i == 6:
				condicion6=True
				lista[i]=input7
			elif i == 7:
				condicion7=True
				lista[i]=input8
			#lista=[input1,input2,input3]#input3.input4,input5,input6,input7,input8
		for i in contenido:
			y+=60
			lista[contador]= eztext.Input(maxlength = 0, color=white, prompt=i)
			lista[contador].set_pos(0,y)
			contador=contador + 1

		contenido = ' '.join(contenido)
		print(contenido)
		salirinput = eztext.Input(maxlength = 1, color=white, prompt=' ')
		eztextrecords = eztext.Input(maxlength = 0, color=white, prompt='')

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


			if presionada[pygame.K_RETURN] and salirinput.value == "0":
				#Devolvemos al menu principal
				return
		eztextrecords.draw(gameDisplay)
		if condicion0==True:
			lista[0].draw(gameDisplay)
			lista[0].update(eventos)
		if condicion1==True:
			lista[1].draw(gameDisplay)
			lista[1].update(eventos)
		if condicion2==True:
			lista[2].draw(gameDisplay)
			lista[2].update(eventos)
		if condicion3==True:	
			lista[3].draw(gameDisplay)
			lista[3].update(eventos)
		if condicion4==True:	
			lista[4].draw(gameDisplay)
			lista[4].update(eventos)
		if condicion5==True:	
			lista[5].draw(gameDisplay)
			lista[5].update(eventos)
		if condicion6==True:	
			lista[6].draw(gameDisplay)
			lista[6].update(eventos)
		if condicion7==True:	
			lista[7].draw(gameDisplay)
			lista[7].update(eventos)
		input4.draw(gameDisplay)
		input5.draw(gameDisplay)
		input6.draw(gameDisplay)
		salirinput.update(eventos)	
		eztextrecords.update(eventos)
		pygame.display.update()
		fpsClock.tick(FPS)
