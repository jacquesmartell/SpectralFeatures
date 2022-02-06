import numpy as np
import Utilities.Spectrum as amplitude

def getFlatness(inSamples, inSampleRate):
    spectrumData = amplitude.getSpectrum(inSamples)
    return np.exp(np.mean(np.log(spectrumData))) / np.mean(spectrumData)
