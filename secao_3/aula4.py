#Tipos int e float
#Sem tem casa decimal é float, senão é int

#int -> número inteiro
#O tipo int representa qualquer número
#positivo ou negativo. int sem sinal é considerado
#positivo.
print(11) #int
print(-11) #int
print(0)

#float -> Número com ponto flutuante
#O tipo float representa qualquer número
#positivo ou negativo com ponto flutuante
#float sem sinal é considerado positivo.
print(1.1) #float / sempre separado por ponto
print(0.0 , -1.5) #float

#A função type mostra o tipo que o Python
#inferiu ao valor.
print(type('Otavio'))#objeto do tipo string
print(type(1))#objeto do tipo int
print(type(1.1), type(-1.1))#objeto tipo float