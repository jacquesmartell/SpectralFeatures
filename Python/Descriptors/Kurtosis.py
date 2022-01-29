import numpy as np
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time
import Descriptors.Centroid as centroid
import Descriptors.Spread as spread

def getKurtosis(inSamples, inSampleRate, inDomain="Frequency"):
    
    if inDomain == "Time":
        spreadData = spread.getSpread(inSamples, inSampleRate, inDomain)
        centroidData = centroid.getCentroid(inSamples, inSampleRate, inDomain)
        timeData = time.getVectorTime(inSamples, inSampleRate)
        return np.sum((timeData - centroidData) ** 4 * inSamples) / (spreadData ** 4 * np.sum(inSamples)) - 3

    elif inDomain == "Frequency":
        spreadData = spread.getSpread(inSamples, inSampleRate, inDomain)
        centroidData = centroid.getCentroid(inSamples, inSampleRate, inDomain)
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        return np.sum((frequencyData - centroidData) ** 4 * spectrumData) / (spreadData ** 4 * np.sum(spectrumData)) - 3