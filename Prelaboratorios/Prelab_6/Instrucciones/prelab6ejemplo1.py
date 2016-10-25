
# Descripcion: Funcion que computa el perimetro de una circunferencia
# Parametros: 
#           r: radio de la circunferencia 
#           pi: Valor de la constante PI 
def perimetro(r: float, pi: float) -> float:
# PRECONDICION: r>0

# var respuesta: float // variable auxiliar
	respuesta = 2 * pi * r 
	return respuesta
# POSTCONDICION: perimetro = 2*pi*r
	
	
# Descripcion: Procedimiento que inicializa un arreglo con el valor cero
# Parametros:
#               l: arreglo a inicializar
def inicializarLista (l:[int]) -> 'void':
# PRECONDICION: true
# POSTCONDICION: (all l[i]==0 for i in range(0,len(l))  
# var i: int
  for i in range(0,len(l)):
     l[i] = 0

##################################
# Inicio del programa 
##################################
# var a: float
a = perimetro( 20.5, 3.141 )
print ("El perimetro de la circunferencia es:",a)

# var l:[int]
l = [1,2,3,4,5]

#Valores en el arreglo antes de la llamada a inicializarLista
print ("La lista se ha declarado con los siguientes valores:",l)

inicializarLista(l)

#Valores en el arreglo después de la llamada a inicializarLista
print ("La lista se ha inicializado en:",l)


