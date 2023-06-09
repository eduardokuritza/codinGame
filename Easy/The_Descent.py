# Adicionando um comentário
import sys
import math

while True:
    x = 0
    y = 0

    for i in range(8):
        mountain_h = int(input())
        if mountain_h > x: 
            x = mountain_h
            y = i

    print(y)