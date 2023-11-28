#Função input para coletar dados

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

#Maneira errada de somar os números 
#Sem dcolocar input dentro do int
#Essa soma vai ser a junção das duas str
#Pois o python não entende com numero
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números é: {numero_1 + numero_2}')

#Exemplo de como fazer a checagem 
#Se ele receber um str em vez de int ele não faz a soma
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_num1 = int(numero_1)
int_num2 = int(numero_2)
print(f'A soma dos números é: {int_num1 + int_num2}')