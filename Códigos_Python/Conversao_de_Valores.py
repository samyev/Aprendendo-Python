#--------------------------------------------------------------------------------------------#
# Funções para conversão de valores, Python fornece algumas funções simples que permitem isso
# As funções int, float e str irão tentar converter seus argumentos para os tipos int, float e
# str. Essas funções são chamadas de conversão de valores.
#--------------------------------------------------------------------------------------------#

# A função int pode converter para um int(inteiro) um argumento numérico em ponto 
# flutuante(float) ou um string(texto).

print(3.14, "Conversão:" ,int(3.14))
print(3.9999, "Conversão:" ,int(3.9999)) # Isto não arredonda para o inteiro mais próximo
print(3.0, "Conversão:" ,int(3.0))
print(-3.999, "Conversão:" ,int(-3.999)) # Observe que o resultado está mais próximo de zero

print("2345", "Conversão:" ,int("2345")) # Examina o string para reproduzir um int
print(20, "Conversão:" ,int(20))         # int também funcona sobre inteiros

#print("Conversão:" ,int("23garrafas"))   # Esta conversão não irá funcionar, pois não temos como
                                          # converter uma letra em um número, então para ver funcionando
print("Conversão:" ,int("23"))    # retire o "garrafas" e deixe somente o 23

