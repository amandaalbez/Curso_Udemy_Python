#Ordem de Precedencia - Ordem que seram calculadas
# 1. (n + n) (os parenteses mais internos serão executados primeiro)
# 2. **
# 3. * / // %
# 4. + - (são os ultimos)

conta_1 = 1 + 1 ** 5 + 5 #7
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) #1024
print(conta_2)