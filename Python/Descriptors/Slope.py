import numpy as np
import Utilities.VectorTime as time
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency

def getSlope(inSamples, inSampleRate, inDomain="Frequency"):

    if inDomain == "Time":
        timeData = time.getVectorTime(inSamples, inSampleRate)
        return sum((timeData - np.mean(timeData)) * (inSamples - np.mean(inSamples))) / np.sum((timeData - np.mean(timeData)) ** 2)

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        return sum((frequencyData - np.mean(frequencyData)) * (spectrumData - np.mean(spectrumData))) / np.sum((frequencyData - np.mean(frequencyData)) ** 2)