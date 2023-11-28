#Indrodução a blocos de código if e else

# if / elif / else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?')

#Condição
if entrada == 'entrar': #Se for verdadeiro ele ira exibir a mensagem
    print('Você entrou no sistema')
elif entrada == 'sair': #elif pode repetir várias vezes
    print('Você saiu do sistema')
else: #caso a pessoa nn digitou uma das duas condições
    print('Você não digitou uma opção')

print('FORA DOS BLOCOS')