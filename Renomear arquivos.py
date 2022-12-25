# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:21:52 2021

@author: vinic
"""

import os
from tqdm import tqdm

path_user = str(input("Current path: ")).replace('\\', '/')
ext_user = str(input("New extension [.xxx]: "))

def get_first_extension(directory):
    first_arq = os.listdir(directory)[0][::-1]   # Pega o nome do arquivo invertido para pegar o último '.''
    dot_position = first_arq.index('.')
    ext = first_arq[:dot_position][::-1]
    return '.' + ext

pos_initial = 1
path = path_user if path_user != '' else "./"
arq = ext_user if ext_user != '' else get_first_extension(path)

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
    
    
    
    
    
    
    
    
    
    
    
    
    
