#Programa para calcular el salario semanal de diferentes cargos en una empresa

#CARGOS: Supervisor - Trabajador - Gerente

#TURNOS:

#///Matutino: 25$xH (Trabajador) - 45$XH (Supervisor)

#///Vespertino: 30$xH (Trabajador) - 50$xH (Supervisor)

#///Nocturno: 40$xH (Trabajador) - 60$xH (Supervisor)

#///El cargo de Gerente posee un pago semanal de 950$ 

#BONOS:

#/// Nocturno: 30% del concepto trabajado en turno nocturno (Trabajador y Supervisor) 

#/// Feriado: 50% del concepto trabajado en los turnos del fin (Trabajador y Supervisor) 

"""DESCRIPCION: Se le pedira al usuario que especifique si es Trabajador, Supervisor 
Gerente. en caso de ser TRABAJADOR o SUPERVISOR: Se le pedira que ingrese las horas
trabajadas en los diferentes turnos (Matutino, Vespertino, nocturno) en caso de no haber
laborado en alguno de esos turnos se coloca un Cero(0). Luego se preguntara si trabajo 
el fin de semana. y ingresara las horas laboradas en los turnos del fin de semana.
En caso de ser GERENTE se le pedira que ingrese el numero de horas extras laboradas"""

#Autor: Jesus Kauze 12-10273@usb.ve 	Alejandro Martinez 13-10839@usb.ve

#Variables:
horas_matutino=0
horas_vespertino=0
horas_nocturnas=0
feriado_matutino=0
feriado_vespertino=0
feriado_nocturnas=0
horas_feriado_matutino=0
horas_feriado_vespertino=0
horas_feriado_nocturnas=0
subtotal_feriado=0
semanal_nocturnas=0
semanal_matutino=0
semanal_vespertino=0

print("\nBienvenido al 'Calculador de salario semanal Por Jesus Y Alejandro'")
print("\nCargos en la empresa: Supervisor - Trabajador -  Gerente")
	#PROGRAMACION ROBUSTA
while True:
	try:
		cargo = input("\nIngrese el cargo del empleado: ")
		cargo=cargo.lower()
		#PRECONDICION
		assert(cargo == "gerente" or cargo == "supervisor" or cargo == "trabajador")
		break
	except:
		print("\nPor favor Ingrese un cargo existente (gerente, supervisor, trabajador):")

print("")

if cargo=="gerente":
	print("El cargo de gerente tiene un pago semanal de 950$")
	print("Adicionalmente se paga 10$ x hora extra laborada")
	print("Como no tiene un turno definido, entre las 6:00am - 12:00am de lunes a viernes puede trabajar 90 horas como maximo")
	
	#PROGRAMACION ROBUSTA
	while True:
		try:
			extra=int(input("\nIntroduzca las horas extras trabajadas: "))
			assert(-1<extra<91) # asegura que no pase del limite
			break
		except:
			print("\nlas horas extras no son validas, por favor coloque un valor posible (entre 0 y 90 horas extras")
	bono_extra=extra*10
	total=950+bono_extra
	
	print("\nSubtotal Semanal: 950$")
	print("Bono hora extra: " + str(bono_extra) +"$")
	print("Total Semanal: " + str(total) + "$")

elif cargo=="supervisor":
	print("El cargo de Supervisor tiene un pago que depende de los turnos:")
	print("----------------------------------------------------------------")
	print("(6:00am - 12:00pm) MATUTINO: 45$ por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("(12:00pm - 6:00pm) VESPERTINO: 50$ por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("(6:00pm - 12:00am) NOCTURNO: 60$ por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("Adicionalmente poseen un bono nocturno de un 30% del total de horas nocturnas trabajadas")
	
	#Entrada Lunes - viernes
	while True:
		try:
			horas_matutino=int(input("\nIntroduzca el total de horas matutinas de lunes a viernes: "))
			horas_vespertino=int(input("Introduzca el total de horas vespertino de lunes a viernes: "))
			horas_nocturnas=int(input("Introduzca el total de horas nocturnas de lunes a viernes: "))
			assert(-1<horas_matutino<31 and -1<horas_vespertino<31 and -1<horas_nocturnas<31) #asegura que no pase de 30
			break
		except:
			print("\ntiene que colocar un valor posible, recuerde que por cada turno como maximo puede alcanzar un total de 0 a 30 horas")

	#Algoritmo lunes - viernes
	
	semanal_matutino = horas_matutino*45
	semanal_vespertino = horas_vespertino*50
	semanal_nocturnas = horas_nocturnas*60 
	
	total_lunes_viernes = semanal_matutino + semanal_vespertino + semanal_nocturnas

	print("\nEl bono feriado se aplica al total de horas trabajadas el fin de semana. el cual se paga un 50% del concepto trabajado")
	
	#Entrada Feriado
	while True:
		try:
			horas_feriado_matutino = int(input("\nIntroduzca las horas matutinas trabajadas el fin de semana (maximo 12 horas)"))
			horas_feriado_vespertino = int(input("Introduzca las horas vespertinas trabajadas el fin de semana (maximo 12 horas)"))
			horas_feriado_nocturnas = int(input("Introduzca las horas nocturas trabajadas el fin de semana (maximo 12 horas)"))
			assert(-1<horas_feriado_matutino<13 and -1<horas_feriado_vespertino<13 and -1<horas_feriado_nocturnas<13) #asegura no pase de 12
			break
		except:
			print("\ntiene que colocar un valor posible, recuerde que por cada turno como maximo el fin de semanal puede alcanzar un total de 0 a 12 horas")

	#Algoritmo bono feriado 
	
	feriado_matutino = horas_feriado_matutino * 45
	feriado_vespertino = horas_feriado_vespertino * 50
	feriado_nocturnas = horas_feriado_nocturnas * 60
	subtotal_feriado = (feriado_matutino + feriado_vespertino + feriado_nocturnas)
	bono_total = subtotal_feriado * 0.50 
	total_con_bono_feriado = bono_total + subtotal_feriado
	
	#Bono nocturno Lunes a viernes + feriado (horas trabajadas en la noche durante TODA LA SEMANA)
	
	bono_nocturno = (semanal_nocturnas + feriado_nocturnas) * 0.30
	
	#TOTAL 
	
	total= total_lunes_viernes + bono_nocturno + total_con_bono_feriado
	
	#Salida
	
	print("\nSubtotal Lunes - viernes: " + str(total_lunes_viernes) +"$")
	print("Bono Nocturno: " + str(bono_nocturno) + "$")
	print("Subtotal Sabado - Domingo: " + str(subtotal_feriado) + "$")
	print("Bono Feriado: " + str(bono_total) + "$")
	print("TOTAL: " + str(total) + "$")
	
elif cargo == "trabajador":
	print("El cargo de Trabajador tiene un pago que depende de los turnos:")
	print("----------------------------------------------------------------")
	print("(6:00am - 12:00pm) MATUTINO: 25$ por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("(12:00pm - 6:00pm) VESPERTINO: 30$ por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("(6:00pm - 12:00am) NOCTURNO: 40 por Hora (maximo 30 horas de lunes a viernes)")
	print("----------------------------------------------------------------")
	print("Adicionalmente posee un bono nocturno de un 30% del total de horas nocturnas trabajadas")
	
	#Entrada
	while True:
		try:
			horas_matutino=int(input("\nIntroduzca el total de horas matutinas de lunes a viernes: "))
			horas_vespertino=int(input("Introduzca el total de horas vespertino de lunes a viernes: "))
			horas_nocturnas=int(input("Introduzca el total de horas nocturnas de lunes a viernes: "))
			assert(-1<horas_matutino<31 and -1<horas_vespertino<31 and -1<horas_nocturnas<31) #asegura no pase de 30
			break
		except:
			print("\ntiene que colocar un valor posible, recuerde que por cada turno como maximo puede alcanzar un total de 0 a 30 horas")

	#Algoritmo 
	
	semanal_matutino = horas_matutino*25
	semanal_vespertino = horas_vespertino*30
	semanal_nocturnas = horas_nocturnas*40 
	
	total_lunes_viernes = semanal_matutino + semanal_vespertino + semanal_nocturnas
	
	print("\nEl bono feriado se aplica al total de horas trabajadas el fin de semana. el cual se paga un 50% del concepto trabajado")
	
	#Entrada Feriado
	while True:
		try:
			horas_feriado_matutino = int(input("\nIntroduzca las horas matutinas trabajadas el fin de semana (maximo 12 horas)"))
			horas_feriado_vespertino = int(input("Introduzca las horas vespertinas trabajadas el fin de semana (maximo 12 horas)"))
			horas_feriado_nocturnas = int(input("Introduzca las horas nocturas trabajadas el fin de semana (maximo 12 horas)"))
			assert(-1<horas_feriado_matutino<13 and -1<horas_feriado_vespertino<13 and -1<horas_feriado_nocturnas<13) #asegura no pase de 12
			break
		except:
			print("\ntiene que colocar un valor posible, recuerde que por cada turno como maximo puede alcanzar un total de 0 a 30 horas")

	#Algoritmo bono feriado 
	
	feriado_matutino = horas_feriado_matutino * 25
	feriado_vespertino = horas_feriado_vespertino * 30
	feriado_nocturnas = horas_feriado_nocturnas * 40
	subtotal_feriado = (feriado_matutino + feriado_vespertino + feriado_nocturnas)
	bono_total = subtotal_feriado * 0.50 
	total_con_bono_feriado = bono_total + subtotal_feriado
	
	#Bono nocturno Lunes a viernes + feriado (horas trabajadas en la noche durante TODA LA SEMANA)
	
	bono_nocturno = (semanal_nocturnas + feriado_nocturnas) * 0.30
	
	#TOTAL 
	
	total= total_lunes_viernes + bono_nocturno + total_con_bono_feriado
	
	#Salida
	
	print("\nSubtotal Lunes - viernes: " + str(total_lunes_viernes) +"$")
	print("Bono Nocturno: " + str(bono_nocturno) + "$")
	print("Subtotal Sabado - Domingo: " + str(subtotal_feriado) + "$")
	print("Bono Feriado: " + str(bono_total) + "$")
	print("TOTAL: " + str(total) + "$")

print("\nGracias por usar el programa. att: Alejandro Martinez and Jesus Kauze")
print("Universidad Simon Bolivar")

#POSTCONDICION
try:
	assert((total == (horas_matutino*25+horas_vespertino*30+horas_nocturnas*40) + (horas_feriado_matutino * 25+horas_feriado_vespertino * 30+horas_feriado_nocturnas * 40 + subtotal_feriado * 0.50) + (semanal_nocturnas +
		 feriado_nocturnas)*0.30) or (total == (horas_matutino*45+horas_vespertino*50+horas_nocturnas*60) + (horas_feriado_matutino * 45+horas_feriado_vespertino * 50+horas_feriado_nocturnas * 60 + subtotal_feriado * 0.50) + (semanal_nocturnas +
		 feriado_nocturnas)*0.30) or (total== 950 + extra*10))
except:
	print("hubo error en los calculos, el servicio tecnico pronto lo solucionara")