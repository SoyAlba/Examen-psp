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
    dic=dict(zip(["vowels","lines","characters","file_stats"],[vowel,line,character,file_stats]))
    print(dic)

def main():
    threads=int(input("Press the number of threads to continue..."))
    with ThreadPoolExecutor(threads) as executor:
        for file in dirs:
            executor.submit(counting, foldel_name + "/" + file)

if __name__ == '__main__':
    main()


