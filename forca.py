# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:16:15 2015

@author: Rafael
"""


from random import randint

import turtle
    
j = turtle.Screen ()
j.screensize (640, 480)

text = open ("entrada.txt", encoding = "utf-8")

y = randint (0,11)

t = text.readlines ()
p = "abc"

d = turtle.Turtle ()
d.penup ()
d.setpos (-200, -200)
d.pendown ()


def linhas ():
            
    for i in p:
        d.forward (25)
        d.penup ()
        d.forward (5)
        d.pendown ()
        
linhas ()

d.penup ()
d.back (25*len (p)+5*len (p))

c = turtle.textinput ("Digite seu chute", "Digite seu chute")

if p.find (c) == True:
    d.write (c)
    

        
        
j.exitonclick ()
        
    
    
    
    
    




