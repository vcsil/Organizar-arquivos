# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:21:52 2021

@author: vinic
"""

import os

pos = 1
path = '/01/finish/pothole'
arq = '.jpg'

l = os.listdir(path)

for nome in l:
    novo_nome = str(pos) + arq
    
    try:
            os.rename(path + '/' + nome, path + '/' + novo_nome )
            pos += 1
    except:
        while novo_nome in l:
            indice = l.index(novo_nome)
            l.pop(indice)
            
            pos += 1
            novo_nome = str(pos) + arq

        os.rename(path + '/' + nome, path + '/' + novo_nome )


    #print("arquivo " + nome + " alterado para " + novo_nome)
    #print(nome)
    #print(novo_nome)
    
    
    
    
    
    
    
    
    
    
    
    
    
