import numpy as np
import Utilities.Spectrum as amplitude
import Utilities.Frequency as frequency
import Utilities.VectorTime as time

def getRollOff(inSamples, inSampleRate, inDomain="Frequency", threshold = 0.95):
        
    if inDomain == "Time":
        timeData = time.getVectorTime(inSamples, inSampleRate)
        cumsum = np.cumsum(inSamples)

        cont = 0
        rolloff = 0
        for accum in cumsum:
            if accum > (cumsum[-1] * threshold):
                rolloff = timeData[cont]
                break
            cont += 1
        return rolloff
    
    elif inDomain == "Frequency":
        spectrumData = amplitude.getSpectrum(inSamples)
        frequencyData = frequency.getFrequency(inSamples, inSampleRate)

        cumsum = np.cumsum(spectrumData)
        cont = 0
        rolloff = 0
        for accum in cumsum:
            if accum > (cumsum[-1] * threshold):
                rolloff = frequencyData[cont]
                break
            cont += 1
        return rolloff