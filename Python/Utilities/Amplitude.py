from scipy.fft import rfft
import numpy as np

def getAmplitude(inSamples):
    return(np.abs(rfft(inSamples)))