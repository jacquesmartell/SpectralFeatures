import numpy as np
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time

def getCentroid(inSamples, inSampleRate, inDomain="Frequency"):
    
    if inDomain == "Time":
        timeData = time.getVectorTime(inSamples, inSampleRate)
        return np.sum(inSamples * timeData) / np.sum(inSamples)

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        return np.sum(spectrumData * frequencyData) / np.sum(spectrumData)