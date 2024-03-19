"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos> f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f 
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')#Preenche 10 Caracteres Esquerda
print(f'{variavel: <10}.')#Preenche 10 carcateres Direita
print(f'{variavel: ^10}.')#Coloca 10 caracteres e centraliza
print(f'{100.458796328589874:.1f}')
