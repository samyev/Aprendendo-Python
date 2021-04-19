# Leia sobre turtle no livro "Como Pensar Como um Cientista da Computação" em referências
import turtle

wn = turtle.Screen()             # Cria uma janela e define seus atributos
wn.bgcolor("lightblue")

# primeira tartaruga
tess = turtle.Turtle()           # Cria tess e define seus atributos
tess.color("violet")
tess.pensize(5)

alex = turtle.Turtle()           # Cria alex

tess.forward(80)                 # tess desenha um triângulo equilátero
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete o triângulo

tess.right(180)                  # tess muda de direção
tess.forward(80)                 # tess se move para longe da origem

alex.forward(50)                 # alex desenha um quadrado
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
