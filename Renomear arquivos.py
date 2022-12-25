# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:21:52 2021

@author: vinic
"""

import os

path_user = str(input("Path: ")).replace('\\', '/')

pos_initial = 1
path = path_user if path_user != '' else "./"
arq = '.jpg'

l = os.listdir(path)

for nome in l:
    novo_nome = str(pos_initial) + arq
    
    try:
            #os.rename(path + '/' + nome, path + '/' + novo_nome )
            pos_initial += 1
    except:
        while novo_nome in l:
            indice = l.index(novo_nome)
            l.pop(indice)
            
            pos_initial += 1
            novo_nome = str(pos_initial) + arq

        #os.rename(path + '/' + nome, path + '/' + novo_nome )


    #print("arquivo " + nome + " alterado para " + novo_nome)
    print(nome)
    print(novo_nome)
    
    
    
    
    
    
    
    
    
    
    
    
    
