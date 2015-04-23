# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:03:42 2015

@author: Rafael
"""
from random import randint

pc = 0
jg = 0
    
while pc < 3 and jg  < 3:
    
    y = randint (1,5)
    
    jogador = input("Estou pronto! Escolha sua jogada (pedra, papel, tesoura, lagarto ou Spock).\n")
    
    x = jogador.upper()
    
   
       
    if y == 1:
        z = "Tesoura"
    if y == 2:
        z = "Papel"
    if y == 3:
        z = "Pedra"
    if y == 4:
        z = "Lagarto"
    if y == 5:
        z = "Spock"


  
    if x == "TESOURA":
        x = 1
    elif x == "PAPEL":
        x = 2
    elif x == "PEDRA":
        x = 3
    elif x == "LAGARTO":
        x = 4
    elif x == "SPOCK":
        x = 5
    else:
        print ("Você escreveu errado.")
        continue
        
    
    print ("Eu escolhi", z)
    
    
    if y == x+1 or y == x-2 or y == x-4 or y == x+3:
        print ("Você ganhou!\n")
        jg += 1
    elif x == y:
        print("Deu empate.\n")
    else:
        print ("Você perdeu.\n")
        pc += 1
    
    print ("Placar:\nComputador: %d x Jogador: %d\n" % (pc, jg))
        
if jg == 3:
    print ("Você ganhou o jogo!")
elif pc == 3:
    print ("Você perdeu o jogo.")
        

