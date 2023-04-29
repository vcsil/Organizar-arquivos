# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:21:52 2021

@author: vinic
"""

import os
import random
from tqdm import tqdm

# Define path
path_user = str(input("Current path: ")).replace('\\', '/')

# Change the extension of all files
extension_file_user = str(input("New extension [.xxx]: "))

# If it’s just to remove the numbers from the name
just_remove_number = bool(int(input("Just remove the number? NO [0] YES [1] ")))

try:
    use_old_name = bool(int(input("Use old name (0) or just number (1)?: ")))
except ValueError:
    use_old_name = bool(int(input("Use old name (0) or just number (1)?: ")))

shuffle = bool(int(input("Shuffle (1) or no shuffle (0)?: ")))


def get_file_extension(filename):
    filename_reverse = filename[::-1]
    dot_position = filename_reverse.index('.')
    ext = filename_reverse[:dot_position][::-1]
    return '.' + ext


def set_number(position, digits):
    number = '{:0>{}}'.format(position, digits)

    return number


def filter_filename(filename):
    filename_reverse = filename[::-1]
    dot_position = filename_reverse.index('.')
    filename_pure = filename_reverse[dot_position+1:][::-1]

    if '.' in filename_pure[:5]:
        filename = filename.replace('feat.', 'feat')
        dot_position = filename.index('.')
        filename_pure = filename_pure[dot_position+1:]
    if ' - ' in filename_pure[:6]:
        trace_position = filename_pure.index(' - ')
        filename_pure = filename_pure[trace_position+3:]
    return filename_pure


def rename_file(filename, pos_file, ext_user, len_file_list, just_remove_num):
    global filename_list, path

    filename_filtered = filter_filename(filename)

    if (just_remove_num):
        new_filename = filename_filtered + ext_user
    else:
        number = set_number(pos_file, len_file_list)
        new_filename = number + ' - ' + filename_filtered + ext_user

    try:
        os.rename(path + '/' + filename, path + '/' + new_filename)
        print('\n' + new_filename)
        return
    except FileNotFoundError:
        pos_file += 1
        print('=-=-'*10)
        rename_file(filename, pos_file, ext_user)

    # print("arquivo " + filename + " alterado para " + new_filename)
    # print('\n' + filename)
    # print(new_filename)


pos_initial = 1
path = path_user if path_user != '' else "./"

filename_list = os.listdir(path)
length_filename_list = len(list(str(len(filename_list))))


if (shuffle):
    random.shuffle(filename_list)
    random.shuffle(filename_list)

if extension_file_user == "":
    for filename in tqdm(filename_list):
        extension_file_user = get_file_extension(filename)
        if extension_file_user != '.py':
            rename_file(filename, pos_initial, extension_file_user,
                        length_filename_list, just_remove_number)

            pos_initial += 1
else:
    for filename in tqdm(filename_list):
        rename_file(filename, pos_initial, extension_file_user,
                    length_filename_list, just_remove_number)

        pos_initial += 1
