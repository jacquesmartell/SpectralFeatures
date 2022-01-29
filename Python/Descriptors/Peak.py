import numpy as np
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time

def getPeak(inSamples, inSampleRate, inDomain="Frequency"):

    if inDomain == "Time":
        timeData = time.getVectorTime(inSamples, inSampleRate)
        peakIndex = np.argmax(np.array(inSamples))
        return timeData[peakIndex]

    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)
        peakIndex = np.argmax(np.array(spectrumData))
        return frequencyData[peakIndex]


    
    