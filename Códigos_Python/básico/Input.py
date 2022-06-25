#---------------------------------------------------------------------------------------
# A função input permite que apresentemos um texto ou prompt ao usuário (prompt string)
# quando a função é executadao texto é exibido. O usuário do programa pode digitar o 
# nome e pressionar a tecla enter. Quando isso o ocorre o texto digitado pelo usuário é
# atribuido a uma variável
#---------------------------------------------------------------------------------------

nome = input("Por favor, entre com o seu nome: ")
print("Olá", nome) # rode o código e insira o seu nome

# Quest: Converta Segundos em Horas, converta o imput str em int

# O input sairá um string
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
# Convertendo o string em inteiro
total_segs = int(segundos_str)

# pegando uma divisão inteira
horas = total_segs // 3600 
# pegando o resto da divisão
segs_restantes = total_segs % 3600
# pegando uma divisão inteira
minutos = segs_restantes // 60
# pegando o resto da divisão
segs_restantes_final = segs_restantes % 60

# imprimindo o resultado
print("Hrs=", horas, "mins=", minutos, "segs=", segs_restantes_final)