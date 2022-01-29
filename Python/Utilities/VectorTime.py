import numpy as np

def getVectorTime(inSamples, inSampleRate):
    print(np.arange(0, len(inSamples), 1) / inSampleRate)
    return np.arange(0, len(inSamples), 1) / inSampleRate