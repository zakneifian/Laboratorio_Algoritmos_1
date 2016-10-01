N = int(input('\n\n\nEste algoritmo calcula la suma de los factoriales desde 0 hasta N.\n\nA continuacion introduzca el numero: '))

suma, fact, k = 0,1,0


assert(N >= 0 and 0<=k<=N)

while k<=N:
	if k>0:
		fact *= k
	suma += fact
	k += 1

print(N, suma, fact, k)

def prod( iterable ): 
	p= 1 
	for n in iterable: 
		p *= n 
	return p 

#error, assert mal explicado
#assert(suma == sum(0<=i<=N for i in prod(1<=j<= i for j)))