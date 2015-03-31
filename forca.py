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
p = t[0].upper ().strip ()
p2 = p
lenp = len (p)


acentoA = "ÃÀÂÁ"
acentoE = "ÉÊ"
acentoO = "ÔÓÕ"
acentoU = "Ú"
acentoC = "Ç"
acentoI = "Í"



for i in p:
    for n in acentoA:
        if n == i:
            p = p.replace (i, "A")
            
    for n in acentoE:
        if n == i:
            p = p.replace (i, "E")
            
    for n in acentoO:
        if n == i:
            p = p.replace (i, "O")
            
    for n in acentoU:
        if n == i:
            p = p.replace (i, "U")

    for n in acentoC:
        if n == i:
            p = p.replace (i, "C")
            
    for n in acentoI:
        if n == i:
            p = p.replace (i, "I")
 

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
d.hideturtle ()


def linhas ():
    
    d.penup ()
    d.setpos (-320, -300)
    d.pendown ()
    
    global lenp
    
    for i in p:
        
        if i == " ":
            d.penup ()
            d.forward (23)
            d.pendown ()
            lenp -= 1
        else:                
            d.forward (20)
            d.penup ()
            d.forward (3)
            d.pendown ()
        
    d.penup ()
    d.back (20*len (p)+3*len (p))

        
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
x.goto (0, 200)
x.write ("Letras chutadas:")
x.goto (0, 150)

frase = turtle.Turtle ()
frase.hideturtle ()
frase.penup ()
frase.goto (0, 100)
frase.pendown ()

chutes = ""

def acharletra (c):
    
    global chutes
    global erros
    global letras    
    
    y = 0
    
    frase.undo ()
    
    if chutes.find (c.upper ()) == -1:    
        while p.find(c, y) != -1:        
            d.forward (p.find (c, y)*20+p.find(c, y)*3)
            d.write (p2[p.find(c, y)], font=("Arial", 20, "bold"))
            d.back (p.find (c, y)*20+p.find(c, y)*3)
            y = p.find (c, y)+1
            letras += 1
            chutes += c
            
            
    else:
        frase.write ("Voce ja chutou esta letra")
        
    if p.find (c) == -1:
        if chutes.find (c.upper ()) == -1:        
            erros += 1        
            desenharforca (erros)
            x.write (c.upper (), font= ("Arial", 15))
            x.forward (17)
            chutes += c.upper ()
            
        else:
            frase.write ("Voce ja chutou esta letra")
    print (erros) 


def restart (x, y):
    if x<120 and x>0 and y<120 and y >0:
        forca.clear
        d.cleary.clear
        x.clear
        linhas ()
        acertarpalavra ()
        
def coor (x, y):
    print (x, y)
        
def acertarpalavra ():
        
    global erros
     
   
    y = turtle.Turtle ()
    y.hideturtle ()
    
    while letras < lenp:
        chute = turtle.textinput ("Digite seu chute", "Digite seu chute")
        if chute == "":
            continue
        acharletra (chute[0].upper ())
       
        if erros == 6:
        
            y.write ("Voce perdeu.\nDigite 'S' para jogar novamente", font= ("Arial", 20))        
            r = turtle.textinput ("'S' para jogar", "")
            if r.upper() == "S":
                forca.clear ()
                d.clear ()
                acertarpalavra ()
            else:
                turtle.bye ()                
   
    if letras == lenp:

        y.write ("Parabens!\nVoce ganhou!\nDigite 'S' para jogar novamente", font= ("Arial", 25))
        n = turtle.textinput ("'S' para jogar", "")
        if n.upper() == "S":
            forca.clear ()
            d.clear ()
            acertarpalavra ()
        else:
            turtle.bye ()
        
    if erros == 6:
        
        y.write ("Voce perdeu.\nDeseja jogar novamente?", font= ("Arial", 25))
       
    forca.clear ()
 
acertarpalavra () 





    
    
        

        
    
    
    
    
    




