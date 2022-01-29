import numpy as np
import math
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time
import Descriptors.Centroid as centroid

def getSpread(inSamples, inSampleRate, inDomain="Frequency"):
    
    centroidData = centroid.getCentroid(inSamples, inSampleRate, inDomain)

    if inDomain == "Time":
        timeData = time.getVectorTime(inSamples, inSampleRate)
        return math.sqrt(np.abs(np.sum((timeData - centroidData) ** 2 * inSamples) / np.sum(inSamples)))

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        return math.sqrt(np.abs(np.sum((frequencyData - centroidData) ** 2 * spectrumData) / np.sum(spectrumData)))