import numpy as np
import Utilities.Spectrum as amplitude

def getEntropy(inSamples):
    spectrumData = amplitude.getSpectrum(inSamples)
    normalizedAmplitude = spectrumData / sum(spectrumData)
    return -np.sum(normalizedAmplitude * np.log(normalizedAmplitude)) / np.log(len(spectrumData))