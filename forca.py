# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:16:15 2015

@author: Rafael
"""


from random import randint

import turtle
    
janela = turtle.Screen ()
janela.screensize (640, 480)

text = open ("entrada.txt", encoding = "utf-8")

sorteio = randint (0,11)

t = text.readlines ()
x = "Sao Paulo"
p = x.upper ()


forca = turtle.Turtle ()
forca.hideturtle ()
forca.penup ()
forca.setpos (-320,-150)
forca.pendown ()
forca.left (90)
forca.forward (400)
forca.right (90)
forca.forward (150)
forca.right (90)
forca.forward (100)


d = turtle.Turtle ()


def linhas ():
    
    d.penup ()
    d.setpos (-320, -300)
    d.pendown ()
            
    for i in p:
        d.forward (25)
        d.penup ()
        d.forward (5)
        d.pendown ()
        
    d.penup ()
    d.back (25*len (p)+5*len (p))

        
linhas ()

def desenharforca (e):
    if e == 1:
        forca.right (90)
        forca.circle (30)
        forca.penup ()
        forca.left (90)
        forca.forward (60)
        forca.pendown ()
    elif e == 2:
        forca.forward (100)
        forca.back (100)
    elif e == 3:
        forca.right (30)
        forca.forward (50)
        forca.back (50)
    elif e == 4:
        forca.left (60)
        forca.forward (50)
        forca.back (50)
        forca.penup ()
        forca.right (30)
        forca.forward (100)
        forca.pendown ()
    elif e == 5:
        forca.right (20)
        forca.forward (60)
        forca.back (60)
    elif e == 6:
        forca.left (40)
        forca.forward (60)

letras = 0
erros = 0 

x = turtle.Turtle ()
x.penup ()
x.hideturtle ()
x.goto (100, 100)

chutes = ""

def acharletra (c):
    
    global chutes
    global erros
    global letras    
    
    y = 0
    while p.find(c, y) != -1:
        if chutes.find (c.upper ()) == -1:
            d.forward (p.find (c, y)*25+p.find(c, y)*5)
            d.write (c.upper(), font=("Arial", 25, "bold"))
            d.back (p.find (c, y)*25+p.find(c, y)*5)
            y += p.find (c)+1
            letras += 1
            chutes += c
        else:
            x.write ("Voce ja chutou esta letra")
        
    if p.find (c) == -1:
        if chutes.find (c.upper ()) == -1:        
            erros += 1        
            desenharforca (erros)
            x.write (c.upper (), font= ("Arial", 20))
            x.forward (20)
            chutes += c.upper ()
            
        else:
            x.write ("Voce ja chutou esta letra")
        
    
        
def acertarpalavra ():   
    
    global erros
    x = turtle.Turtle ()
    x.hideturtle ()
    
    while letras < len (p):
        chute = turtle.textinput ("Digite seu chute", "Digite seu chute")
        acharletra (chute[0].upper ())
        print (len (p))
        
    if letras == len (p):

        x.write ("Parabens!\nVoce ganhou!\nDeseja jogar novamente?", font= ("Arial", 35))
   
    if erros == 6:
        print (erros)
        x.write ("Voce perdeu.\nDeseja jogar novamente?")
        
        for i in range (5):
            forca.undo ()
    
acertarpalavra () 


    
    
        

        
    
    
    
    
    




