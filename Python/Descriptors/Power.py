import numpy as np

def getPower(inSamples, inSampleRate):
    return np.sum(inSamples**2) / (2 * len(inSamples) + 1)