# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:16:15 2015

@author: Rafael
"""

import turtle

j = turtle.Screen ()

def desenho (x=-300, l=60, l2=30, l3=-45):
    
    c1 = turtle.Turtle ()
    c1.color ("black")
    c1.hideturtle ()
    c1.speed (1000000)
    c1.penup ()
    c1.goto (x,-150)
    c1.pendown ()
    c1.left (l)
    c1.forward (120)
    c1.left (l2)
    c1.forward (180)
    c1.right (90)
    c1.circle (50)
    c1.left (l3)
    c1.forward (100)
    
desenho ()
desenho (-180, 120, -30, 225)
    
j.exitonclick ()
    