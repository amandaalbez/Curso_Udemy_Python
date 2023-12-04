# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o  #Posição
# -6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-4])#os dois retonr a letra a

print('á' in nome) #Conferir se a letra á esta em nome
print('z' in nome) #False não esta em nome

print('vio' not in nome) #False ele ESTA em nome

#Joguinho 
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')