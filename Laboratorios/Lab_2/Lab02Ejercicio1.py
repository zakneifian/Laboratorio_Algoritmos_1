esDescendienteExtranjero = True #Determina si es extranjero y es de tipo booleano
edad = 30 #Determina la edad de la persona y es de tipo entero
puedeVotar = True #Determina si puede votar y es de tipo booleano

#Precondicion
assert(0 < edad < 120)

#-------------------------------------------

#condicional que determina si es descendiente o no de extranjeros y su rango de edad para votar
if esDescendienteExtranjero and edad >= 25:
	pass 
elif esDescendienteExtranjero and  edad < 25:
	puedeVotar = False
elif not esDescendienteExtranjero and edad >= 18:
	pass
else: #No es descendiete extranjero y edad menor a 18
	puedeVotar = False

# condicional que imprime si puede o no votar
if puedeVotar:
	print("La persona puede votar")
elif not puedeVotar:
	print("La persona no puede votar")
#-------------------------------------------

#Postcondicion
assert(puedeVotar == True or puedeVotar == False)