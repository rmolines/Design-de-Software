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
p = "banana"

forca = turtle.Turtle ()
forca.penup ()
forca.setpos (-300,-150)
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
    d.setpos (-200, -200)
    d.pendown ()
            
    for i in p:
        d.forward (25)
        d.penup ()
        d.forward (5)
        d.pendown ()
        
    d.penup ()
    d.back (25*len (p)+5*len (p))

        
linhas ()

def desenharforca ():
    

letras = 0
    

def acharletra (c):
    
    global letras    
    
    y = 0
    while p.find(c, y) != -1:
        d.forward (p.find (c, y)*25+p.find(c, y)*5)
        d.write (c.upper(), font=("Arial", 25, "bold"))
        d.back (p.find (c, y)*25+p.find(c, y)*5)
        y += p.find (c)+1
        letras += 1
    
        
            
    
        
def acertarpalavra ():   
    
    
    while letras < len (p):
      
        chute = turtle.textinput ("Digite seu chute", "Digite seu chute")
        acharletra (chute)
    
acertarpalavra () 


    
    
        
janela.exitonclick ()
        
    
    
    
    
    




