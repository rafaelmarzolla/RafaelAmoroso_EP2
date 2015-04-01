# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:49:48 2015

@author: rafaelmarzolla
"""

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-300,-300)
tartaruga.pendown()
tartaruga.color("orange")

dist = 200


for i in range(1):

    tartaruga.forward(100) # Avança a distancia pedida base
    tartaruga.left(180) #vira na direção contraria
    tartaruga.forward(50)#vai até a metade
    tartaruga.right(90)#vira pra cima
    tartaruga.forward(300) #anda pra cima
    tartaruga.right(90) #vira para a direita
    tartaruga.forward(120) #anda pra frente
    tartaruga.right(90) #vira pra baixo
    tartaruga.forward(60) #anda 
    tartaruga.setpos(-150,-60)   
    tartaruga.circle(20)    #cabeça
    tartaruga.setpos(-130,-80)
    tartaruga.forward(40) #tronco
    tartaruga.left(35) #angulo dos braços
    tartaruga.forward(30) #tamanho dos braços
    tartaruga.left(180)
    tartaruga.forward(30)
    tartaruga.left(115)   
    tartaruga.forward(30)
    tartaruga.back(30)
    tartaruga.left(30)
    tartaruga.forward(60)
    tartaruga.left(20)
    tartaruga.forward(50)
    tartaruga.back(50)
    tartaruga.right(50)
    tartaruga.forward(50)
    window.exitonclick()
