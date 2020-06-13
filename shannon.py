#This is an attempt to implement entropy rate of a source according to Shannon
#The functions will be implemented according to the nth-order models. It is 
#a work in progress. 

import math
freqdist = {
    'E': 12.02,
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 7.31,
    'N': 6.95,
    'S': 6.28,
    'R': 6.02,
    'H': 5.92,
    'D': 4.32,
    'L': 3.98,
    'U': 2.88,
    'C': 2.71,
    'M': 2.61,
    'F': 2.30,
    'Y': 2.11,
    'W': 2.09,
    'G': 2.03,
    'P': 1.82,
    'B': 1.49,
    'V': 1.11,
    'K': 0.69,
    'X': 0.17,
    'Q': 0.11,
    'J': 0.10,
    'Z': 0.07
}

def zeroOrder(size):
    rate = math.log2(size)
    print("The entropy rate is: \t{:.4f}".format(rate))

def firstOrder(size):
    rate = 0
    for i in freqdist:
        print(rate)
        rate += -((freqdist[i] / size) * math.log2((freqdist[i] / size)))
    print("The entropy rate is: \t{:.4f}".format(rate / 2))

firstOrder(27)
