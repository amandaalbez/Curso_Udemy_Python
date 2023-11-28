#Conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float, bool

print(1 + 1) #ele entende que é int então irá efetuar a soma
print('a' + 'b') #ele entende que é uma string e ele uniu "ab"

#Ele só contatenar tipos iguais str com str, int com int

print(int('1'), type(int('1')))#correção do tipo
print(int('1') + 1) #recebendo str convertendo para int e somando(2)
print(float('1') + 1) #recebendo str convertendo para float e somando(2.0)

#Ele executa de dentro pra fora, executando o () dentro primeiro

print(bool(' ')) #String vazia = False / String com caracter = True

print(str(11) + 'b') #Coverte int para str = (11b)






