#----------------------------------------------------------------------------------------
# Neste exemplo o for percorre uma lista de strings que na verdade são cores interpretadas
# pela biblioteca turtle, assim a casa iteração alex (a tartaruga) mudara de cor
#----------------------------------------------------------------------------------------

# leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle            # cria alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]: # repita 4 vezes
   alex.color(aColor)            # modifica cor de alex a cada iteração
   alex.forward(50)              # faz alex andar pra frente
   alex.left(90)                 # faz alex rodar 90 graus pra esquerda

wn.exitonclick()