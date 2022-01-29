from scipy.fft import rfft
import numpy as np

def getSpectrum(inSamples):
    return(np.abs(rfft(inSamples)))