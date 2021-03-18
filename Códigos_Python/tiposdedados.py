#-----------------------------------------------------------------------------------------------------------------#
# Em python, existem tipos de dados, que são diferentes, como um "int" = inteiro, "string" = texto, "float" = números
# com ponto flutuante, como 1.2, 2.3. Mas em python não precisamos especificar o tipo de dado que queremos para as
# variáveis, o interpretador pyhton entende.
#-----------------------------------------------------------------------------------------------------------------#

# Para ter mais certeza sobre qual classe um valor pertence, pyhton possui uma função chamada "type", que descreve
# o tipo de classe aquee=le valor pertence

print(type("Olá, mundo!")) # Para se escrever uma string se usa aspas "" e se escreve dentro dela "Olá", pode se usar
                           # também entre apóstrofos 'Olá' ou trêS de cada '''Olá''' e """Olá""" 
print (type(2021))

print("Olá, mundo!") # Para imprimir esta string se uma "print" assim ele mostrará esta string na tela
print('''Olá, mundo!''')

# Strings com aspas pode conter apóstrofos, e strings com apóstrofos podem conter aspas

print('''"Oh nao", exclamou ela, "A bicleta esta quebrada!"''')