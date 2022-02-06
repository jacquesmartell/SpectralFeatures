import numpy as np

def getEnergy(inSamples, inSampleRate):
    return np.sum(inSamples**2)