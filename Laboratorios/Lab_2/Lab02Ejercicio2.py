tiempoLlamada = 17 #Determina la longitud de la llamada
turno = "matutino" #Determina que turno es
dia = "lunes" #Determina que dia es
diaFeriado = False #Determina si entre semana, es un dia feriado

#Precondicion
assert(tiempoLlamada  > 0 and isinstance(tiempoLlamada, int))

#condicional que determina el cobro segun la longitud de la llamada
if tiempoLlamada <= 5:
	cobro = tiempoLlamada*1.00
elif 5 < tiempoLlamada <= 8:
	tiempoLlamada = tiempoLlamada - 5
	cobro = 5*1.00 + tiempoLlamada*0.8
elif 8 < tiempoLlamada <= 10:
	tiempoLlamada = tiempoLlamada - 8
	cobro = 5*1.00 + 3*0.8 + tiempoLlamada*0.7
else: # tiempoLlamada > 10
	tiempoLlamada = tiempoLlamada - 10
	cobro = 5*1.00 + 3*0.8 + 2*0.7 + tiempoLlamada*0.5

#-------
if dia == "domingo":
	cobro = cobro*0.03 + cobro
elif dia != "domingo" and dia != "sabado" and not diaFeriado:
	if turno == "matutino":
		cobro = 0.15*cobro + cobro
	elif turno == "vespertino":
		cobro = 0.10 + cobro
	else: #Cualquier otro turno que no sea matutino o vespertino
		pass
else: #El caso en el que es un dia feriado o sabado
	pass

cobro = round(cobro, 7) #elimina el error de float generado por como la computadora
#						 calcula los numeros binariamente redondeando, en este caso, a 7 decimales
#------------------------------------------------------
print("La persona ha de pagar $" + str(cobro))

#Postcondicion
assert(cobro > 0 and isinstance(cobro, float))
