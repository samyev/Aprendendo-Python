# Rode este código no terminal

# leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle           # permite usar as funções e objetos do módulo turtle

wn = turtle.Screen()     # cria uma janela gráfica
alex = turtle.Turtle()   # cria um turtle chamado alex
alex.forward(150)        # manda o alex se mover 150 unidades para frente
alex.left(90)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo

# exercicio: complete o retângulo
alex.left(90)
alex.forward(150) 
alex.left(90) 
alex.forward(75)

wn.exitonclick()