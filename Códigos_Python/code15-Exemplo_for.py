#---------------------------------------------------------------------------------------------
# Neste exemplo o for percorre uma lista, que possui 4 número, assim, ele faz 4 iterções
# fazendo com que o bloco de códifo dentro dele, seja executado 4 vezes.
#---------------------------------------------------------------------------------------------

# leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle             # Cria alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0,1,2,3]:       # Repita o código 4 vezes
  alex.forward(50)        # faz alex andar pra frente
  alex.left(90)           # faz alex rodar 90 graus pra esquerda

wn.exitonclick()