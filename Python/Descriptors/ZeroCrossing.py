import numpy as np

def getZeroCrossing(inSamples, inSampleRate):
    anterior = 0
    suma = 0
    for sample in inSamples:
        value = getSign(sample) - anterior
        value = abs(value)
        suma += value
        anterior = getSign(sample)
    
    return suma / len(inSamples)

def getSign(inValue):
    value = 0

    if inValue > 0:
        value = 1
    
    if inValue < 0:
        value = -1
    
    return value