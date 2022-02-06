import numpy as np
import Utilities.Spectrum as amplitude
import antropy as ant
import math

def getEntropy(inSamples, inSampleRate, inDomain="Frequency"):

    if inDomain == "Time":

        normalizedAmplitude = inSamples / np.sum(inSamples)

        newNormalizedAmplitude = []
        for sample in normalizedAmplitude:
            if sample != 0:
                newNormalizedAmplitude.append(abs(sample))

        return -np.sum(newNormalizedAmplitude * np.log(newNormalizedAmplitude)) / np.log(len(newNormalizedAmplitude))

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        normalizedAmplitude = spectrumData / sum(spectrumData)
        return -np.sum(normalizedAmplitude * np.log(normalizedAmplitude)) / np.log(len(spectrumData))