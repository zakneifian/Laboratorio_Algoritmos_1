#Valores inciales
N = int(input('\n\n\nEste algoritmo calcula la suma de los factoriales desde 0 hasta N.\n\nA continuacion introduzca el numero: '))
suma, fact, k = 0,1,0

#Pre
assert(N >= 0 and 0<=k<=N)

#Algo
while k<=N:
	if k>0:
		fact *= k
	suma += fact
	k += 1

#Print que no estara en la version final para hacer track a los valores
print(N, suma, fact, k)

#Funcion que definio el profesor que aparece creada por otro en: http://stackoverflow.com/questions/595374/whats-the-python-function-like-sum-but-for-multiplication-product
def prod( iterable ): 
	p= 1 
	for n in iterable: 
		p *= n 
	return p 


#error en Post, mal argumento?
assert(suma == sum(0<=i<=N for i in prod(1<=j<= i for j)))

#Saluda
print("El factorial es:", fact)