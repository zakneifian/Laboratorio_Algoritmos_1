"""
 El "náufrago" ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo 
de $20.00, $25.00 y $30.00 respectivamente. La empresa acepta tarjetas de débito con un cargo 
de 5% sobre la compra sino pasa de $250 y tarjetas de crédito con un cargo de 10% sobre la compra 
sino pasa de $500 sobre la compra. Considere que los clientes pueden adquirir varios tipos de 
hamburguesas, implemente un algoritmo en Python para determinar cuánto debe pagar un persona 
por N hamburguesas para un tipo de pago TP ∈ {“Efectivo”,”Debito”, “Credito”}. 
Considere que N es un número de 6 dígitos d1, d2, d3, d4, d5 y d6, N = d1d2d3d4d5d6, donde
d1d2 corresponden al número de hamburguesas sencillas, d3d4 al número de hamburguesas 
dobles y d5d6 al número de hamburguesas triples. Por ejemplo: 
a) Sea N = 50310, donde d1d2 = 05, d3d4 = 03 y d5d6 = 10 
b) Sea N = 3, donde d1d2 = 00, d3d4 = 00 y d5d6 = 03 
Pista: Considere que N es un número decimal y por lo tanto N = p*q + r, donde q = 10.
"""
d1=d2=d3=d4=d5=d6=None
TP = "Debito"
N = 251
#Precondicion asegura que TP tenga un valor correcto y N tambien
assert((TP == "Efectivo" or TP == "Debito" or TP == "Credito") and 0 < int(N) < 999999)

#Con este condicional verifico la longitud de N y voy separando usando modulos y los numeros anteriores
if N < 10:
	d6 = N
elif N < 100:
	d6 = N%10
	d5 = int(N/10)
elif N < 1000:
	d6 = N%10
	d5 = int((N%100 - d6)/10)
	d4 = int(N/100)
elif N < 10000:
	d6 = N%10
	d5 = int((N%100 - d6)/10)
	d4 = int((N%1000 - d5)/100)
	d3 = int(N/1000)
elif N < 100000:
	d6 = N%10
	d5 = int((N%100 - d6)/10)
	d4 = int((N%1000 - d5)/100)
	d3 = int((N%10000 - d4)/1000)
	d2 = int(N/10000)
elif N < 1000000:
	d6 = N%10
	d5 = int((N%100 -d6)/10)
	d4 = int((N%1000 - d5)/100)
	d3 = int((N%10000 - d4)/1000)
	d2 = int((N%100000 - d3)/10000)
	d1 = int((N%1000000 - d2)/100000)
else: #Ningun caso tiene mas de 999999 o menos de 0 pero igual puse el else
	pass


if 9999 > N > 100000:
	d1d2 = int(str(d1) + str(d2))
	d3d4 = int(str(d3) + str(d4))
	d5d6 = int(str(d5) + str(d6))
	sencillas = d1d2 * 20
	dobles = d3d4 * 25
	triples = d5d6 * 30
	subtotal = sencillas + dobles + triples

	#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal

elif 999 > N > 10000:
	d3d4 = int(str(d3) + str(d4))
	d5d6 = int(str(d5) + str(d6))
	sencillas = d2 * 20
	dobles = d3d4 * 25
	triples = d5d6 * 30
	subtotal = sencillas + dobles + triples

	#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal

elif 99 > N > 1000:
	d3d4 = int(str(d3) + str(d4))
	d5d6 = int(str(d5) + str(d6))
	dobles = d3d4 * 25
	triples = d5d6 * 30
	subtotal = dobles + triples

	#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal

elif  9 > N > 100:
	d5d6 = int(str(d5) + str(d6))
	dobles = d4*25
	triples = d5d6 * 30
	subtotal = dobles + triples

	#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal

elif  0 > N > 10:
	d5d6 = int(str(d5) + str(d6))
	triples = d5d6 * 30
	subtotal = triples

	#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal

elif  N > 1:
	triples = d6*30
	subtotal = triples

		#Con este condicional se calcula los bonos extras de pago si se usa TDC, etc
	if TP == "Efectivo":
		total = subtotal
	elif TP == "Debito" and subtotal < 250:
		total = 0.05*subtotal + subtotal
	elif TP == "Credito" and subtotal < 500:
		total = 0.1*subtotal + subtotal
	else: #Es debito con mas de 250 o credito con mas de 500
		total = subtotal
else: #No existe ningun caso que cumpla esto pero me parece estetico colocarlo
	pass

print("El cliente debe a pagar un total de $" + str(total))

#Postcondicion
assert(total >= 0) #asegura que se haya calculado y no sea un numero ilogico