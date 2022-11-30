import os, sys
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor

foldel_name="/home/alba/GIT/ExamenPSP/carpeta"
dirs = os.listdir( foldel_name )

def counting(filename):

    txt_file = open(filename)
    file_stats = os.stat(filename)

    vowel = 0
    line = 0
    character = 0

    vowels_list = ['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U']

    for alpha in txt_file.read():

        if alpha in vowels_list:
            vowel += 1

        elif alpha not in vowels_list and alpha != "\n":
            character += 1

        elif alpha == "\n":
            line += 1

    print("Number of vowels in ", filename, " = ", vowel)
    print("New Lines in ", filename, " = ", line)
    print("Number of characters in ", filename, " = ", character)
    print(file_stats)
    print(f'File Size in Bytes is {file_stats.st_size}')
    print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

with ThreadPoolExecutor(10) as executor:  
    for filename in dirs:  
        executor.submit(counting, filename)
    for result in executor.map(counting(filename), dirs):
        print(result)

