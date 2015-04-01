# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:49:48 2015

@author: rafaelmarzolla
"""
import random
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black") #cor do fundo
window.title("Forca") #titulo da janela
variavel_texto = window.textinput("Nome Janela", "Texto Pergunta")

tartaruga = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga2 = turtle.Turtle()
tartaruga2.color("green")

def desenhar_forca():
    
    tartaruga.speed(5)  # define a velocidade
    tartaruga.penup()       
    tartaruga.setpos(-300,-300)
    tartaruga.pendown()
    tartaruga.color("pink") #cor da tartaruga
desenhar_forca()

arquivo = open("entrada.txt", encoding="utf-8")
r = arquivo.readlines()
x = random.choice (r)


tartaruga.setpos(-300,-150)

tartaruga.forward(20)

acertos = 0
erro = 0

while erro<9 and acertos !=len(x):
    t = str(window.textinput("caixa de texto", "digite a letra"))
    for i in range(0, len (x)):
        if t == x[i]:

            tartaruga2.penup()
            tartaruga2.setpos(-150+30*i, -25)
            tartaruga2.pendown()
            tartaruga2.write(t, move=True, align="left",font=("Arial"))
    
    if t not in x:

        erro+=1

    if t in x:
        
        acertos+=1        
    if erro>9:
        window.textinput("vc perdeu", "vc perdeu")
        
    if acertos==x:
        window.textinput("vc ganhou", "vc ganhou")
        
def desenhar_forca():
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
        tartaruga.color("red")
desenhar_forca()
#tartaruga.setpos(-80,-300)

def erro():
    if erro==1:  #cabeça 
    
        tartaruga.setpos(-150,-60)   
        tartaruga.circle(20)    #cabeça
    
    if erro==2:#tronco
    
        tartaruga.setpos(-130,-80)
        tartaruga.forward(40) #tronco
   
    if erro==3:
    
        tartaruga.left(35) #angulo dos braços
        tartaruga.forward(30) #tamanho dos braços

    if erro==4:
    
        tartaruga.left(180)
        tartaruga.forward(30)

    if erro==5:
    
        tartaruga.left(115)   
        tartaruga.forward(30)

    if erro==6:
    
        tartaruga.back(30)
        tartaruga.left(30)

    if erro==7:
    
        tartaruga.forward(60)
        tartaruga.left(20)

    if erro==8:
    
        tartaruga.forward(50)
        tartaruga.back(50)

    if erro==9:
    
        tartaruga.right(50)
        tartaruga.forward(50)

erro()        

window.exitonclick()
