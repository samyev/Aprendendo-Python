#---------------------------------------------------------------------------------------
# As vezes precisamos realizar operações gigantescas, que precisam ser levados em conta
# a ordem que elas irão ser calculadas, para isso existe as regras de precedência
#---------------------------------------------------------------------------------------

# Expressões dentro de parênteses são calculadas primeiro
print(2*(3-1))

# Exponenciação  tem a segunda precedência mais altas
exemplo1 = 2**1+1  #resposta é 3 e não 4
print("Exemplo1: ", exemplo)

# Multiplicação e ambas as divisões têm a mesma precedência, que são mais altas que adição e subtração
exemplo2 = 2*3-1  #resposta é 5 e não 4
print("Exemplo2: ", exemplo2)

# Operadores com a mesma precedência como multiplicação e divisão 
# são executados da esquerda para a direita

exemplo3 = 6-3+4  #subtração é realizada primeiro
print("Exemplo3: ", exemplo3)

exemplo4 = 6-(3+2)  #resposta é 1
print("Exemplo4: ", exemplo4)

print("Exemplo5: ", 2 ** 3 ** 2)     # o ** mais à direita é executado primeiro!
print("Exemplo6: ", (2 ** 3) ** 2)   # use parênteses para forçar a ordem desejada!