import numpy as np
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time
import Descriptors.Centroid as centroid
import Descriptors.Spread as spread

def getSkewness(inSamples, inSampleRate, inDomain="Frequency"):
    
    if inDomain == "Time":
        spreadData = spread.getSpread(inSamples, inSampleRate, inDomain)
        centroidData = centroid.getCentroid(inSamples, inSampleRate, inDomain)
        timeData = time.getVectorTime(inSamples, inSampleRate)
        return np.sum((timeData - centroidData) ** 3 * inSamples) / (spreadData ** 3 * np.sum(inSamples))

    elif inDomain == "Frequency":
        spreadData = spread.getSpread(inSamples, inSampleRate, inDomain)
        centroidData = centroid.getCentroid(inSamples, inSampleRate, inDomain)
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        return np.sum((frequencyData - centroidData) ** 3 * spectrumData) / (spreadData ** 3 * np.sum(spectrumData))