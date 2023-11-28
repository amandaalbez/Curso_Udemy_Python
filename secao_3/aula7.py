#Variaveis são usadas para salvar algo na mem´ria do computador.
#PEP8: inicie variáveis com letras minúsculas, pode usar
#números e underline _.
#O sinal de = é o operador de atribuição. Ele é usado para 
#atribuir um valor a um nome (variável).
#Uso: nome_variavel = expressão

nome_completo = 'Amanda Alcântara'
soma = 2 + 2
print(nome_completo) # Amanda Alcantara
print(soma) # 4

#Variaveis não são usadas para abreviar código
#E sim para deixar o código mais legivel e menos repetitivo
#Só preciso alterar em um lugar o código ], ficando menos repetitivo
int_um = int('1')
print(int_um , type(int_um))


nome = 'Amanda'
idade = 30
maior_de_idade = idade >= 18
print('Nome: ',nome, 'Idade: ',idade)
print('É maior? ',maior_de_idade) #True pois é bool