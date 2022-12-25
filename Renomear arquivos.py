# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:21:52 2021

@author: vinic
"""

import os
from tqdm import tqdm

path_user = str(input("Current path: ")).replace('\\', '/')
extension_file_user = str(input("New extension [.xxx]: "))

try:
    use_old_name = bool(int(input("Use old name (0) or just number (1)?: ")))
except ValueError:
    use_old_name = bool(int(input("Use old name (0) or just number (1)?: ")))


def get_file_extension(filename):
    filename_reverse = filename[::-1]
    dot_position = filename_reverse.index('.')
    ext = filename_reverse[:dot_position][::-1]
    return '.' + ext

def get_first_extension(directory):
    first_arq = os.listdir(directory)[0]
    return get_file_extension(first_arq)


pos_initial = 1
path = path_user if path_user != '' else "./"

filename_list = os.listdir(path)

def rename_file(filename_list, pos_initial, ext_user):
    novo_nome = str(pos_initial) + ext_user
    
    try:
            #os.rename(path + '/' + filename, path + '/' + novo_nome )
            pos_initial += 1
    except:
        while novo_nome in filename_list:
            indice = filename_list.index(novo_nome)
            filename_list.pop(indice)
            
            pos_initial += 1
            novo_nome = str(pos_initial) + ext_user

        #os.rename(path + '/' + filename, path + '/' + novo_nome )


    #print("arquivo " + filename + " alterado para " + novo_nome)
    print(filename)
    print(novo_nome)
    exit()

if extension_file_user == "":
    for filename in tqdm(filename_list):
        extension_file_user = get_file_extension(filename)
        rename_file(filename_list, 1, extension_file_user)
else:
    for filename in tqdm(filename_list):
        rename_file(filename_list, 1, extension_file_user)