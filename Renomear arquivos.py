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

def filter_filename(filename):
    filename_reverse = filename[::-1]
    dot_position = filename_reverse.index('.')
    filename_pure = filename_reverse[dot_position+1:][::-1]
    if '.' in filename_pure[:5]:
        filename = filename.replace('feat.', 'feat')
        filename_reverse = filename[::-1]
        dot_position = filename_reverse.index('.')
        filename_pure = filename_pure[dot_position:]
    return filename_pure

def rename_file(filename, pos_initial, ext_user):
    global filename_list
    
    number = '0' + str(pos_initial) if pos_initial < 10 else str(pos_initial)
    filename_filtered = filter_filename(filename)
    
    new_filename = number + ' - ' + filename_filtered + ext_user
    
    try:
            #os.rename(path + '/' + filename, path + '/' + new_filename )
            print('\n' + new_filename)
            return 
    except:
        pos_initial += 1
        print('=-=-'*10)
        rename_file(filename, pos_initial, ext_user)

    #print("arquivo " + filename + " alterado para " + new_filename)
    #print('\n' + filename)
    #print(new_filename)

if extension_file_user == "":
    for filename in tqdm(filename_list):
        extension_file_user = get_file_extension(filename)
        if extension_file_user != '.py':
            rename_file(filename, pos_initial, extension_file_user)
            pos_initial += 1
else:
    for filename in tqdm(filename_list):
        rename_file(filename, pos_initial, extension_file_user)
        pos_initial += 1