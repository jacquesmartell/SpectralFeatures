import numpy as np
import Utilities.Spectrum as amplitude
import Descriptors.Peak as peak

def getCrest(inSamples, inSampleRate, inDomain="Frequency"):

    if inDomain == "Time":
        peakValue = peak.getPeak(inSamples, inSampleRate, inDomain=inDomain)
        return peakValue / np.mean(inSamples)

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        peakValue = peak.getPeak(inSamples, inSampleRate, inDomain=inDomain)
        return peakValue / np.mean(spectrumData)