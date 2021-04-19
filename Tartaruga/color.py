# Leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle

# exercicio: pergunte ao usuário a cor que ele deseja para o screen
color = input("Qual cor você deseja para o screen? ")
wn = turtle.Screen()
wn.bgcolor(color)         # define a cor de fundo da janela

# exercicio: pergunte ao usuário a cor que ele deseja para o a tartaruga tess
color_turtle = input("Qual cor você deseja para a tartaruga? ")
tess = turtle.Turtle()
tess.color(color_turtle)               # tess fica azul

# exercicio: pergunte ao usuário a espessura da caneta, e tranforme em int
espesura = int(input("Qual espessura você deseja para a caneta? "))
tess.pensize(3)                  # define a espessura da caneta

tess.forward(150)
tess.left(90)
tess.forward(75)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(75)

wn.exitonclick()