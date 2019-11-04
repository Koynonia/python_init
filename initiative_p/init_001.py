import sys
from math import cos, radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

# Imprime Hello e pergunta o meu nome.

print("Hello, Visual Studio")
print()
print('Qual o seu nome?') # pergunta o nome
myName = input()
print()
print('Como é bom conhecer você, ' + myName)
print('O tamanho do seu nome em caracteres é: ' + str(len(myName)))
print()
print('Qual a sua idade?') # pergunta a idade
myAge = input()
print()
print('Você irá fazer ' + str(int(myAge) + 1) + ' em um ano.')

# Create a string with spaces proportional to a cosine of x in degrees

#for i in range(360):
#    print(cos(radians(i)))

def make_dot_string(x):
    rad = radians(x)                             # cos works with radians
    numspaces = int(20 * cos(rad) + 20)          # scale to 0-40 spaces
    st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
    return st

#def main():
#    for i in range(0, 1800, 12):
#        s = make_dot_string(i)
#        print(s)

#main()

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()