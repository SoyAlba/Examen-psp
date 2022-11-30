import time
import queue
import random
import logging
import threading
from random import randint, randrange
import math

queue = queue.Queue(maxsize=10)


def producer():
    while True:
        if not queue.full():
            x = random.randint(10, 1000)
            queue.put(x)

            time.sleep(1)


def consumer():
    while True:
        if not queue.empty():
            num1 = queue.get()
            num2 = queue.get()
            num3 = queue.get()
            num4 = queue.get()
            queue.task_done()
            time.sleep(10)
            print("El MCD de ", num1, " , ", num2," , ", num3," y ", num4," es: ", mcd_n(n=(num1, num2, num3, num4)))


def mcd(n1, n2):
    if n1 < n2:
        i = n1
    else:
        i = n2
    while not (n1 % i == 0 and n2 % i == 0):
        i -= 1
    else:
        return i
def mcd_n(n):
    numeros = list(n)
    resultado = mcd(numeros[0], numeros[1])
    if len(numeros) > 2:
        for n in numeros[2:]:
            resultado = mcd(resultado, n)
    return math.fabs(resultado)


if __name__ == '__main__':
    
        thread_producer = threading.Thread(target=producer)
        thread_producer.start()

        thread_consumer = threading.Thread(target=consumer)
        thread_consumer.start()
