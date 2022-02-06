import numpy as np

def getVectorTime(inSamples, inSampleRate):
    return np.arange(0, len(inSamples), 1) / inSampleRate