#----------------------------------------------------------------------------------------
# Neste exemplo mesmo que o for percorra uma lista de strings ainda sim ele esta fazendo 4 
# iteraçẽos, assim ele acaba fazendo com que o código execute 4 vezes.
#----------------------------------------------------------------------------------------

# leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
    alex.forward(50)      # faz alex andar pra frente
    alex.left(90)         # faz alex rodar 90 graus pra esquerda

wn.exitonclick()