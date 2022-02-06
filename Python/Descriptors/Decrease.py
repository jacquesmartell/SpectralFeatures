import numpy as np
import Utilities.Spectrum as amplitude

def getDecrease(inSamples, inSampleRate, inDomain="Frequency"):

    if inDomain == "Time":

        N = len(inSamples)
        cero = inSamples[0]
        inSamplesNew = np.delete(inSamples, 0)

        numNume = []
        for sample in inSamplesNew:
            numNume.append(sample - cero)
        
        denNum = np.arange(1, N, 1)
        denominador = np.sum(inSamplesNew)

        suma = 0
        for i in range(len(numNume)):
            divi = numNume[i]/denNum[i]
            suma += divi

        return suma / denominador

    elif inDomain == "Frequency":
        
        spectrumData = amplitude.getSpectrum(inSamples)

        N = len(spectrumData)
        cero = spectrumData[0]
        spectrumData = np.delete(spectrumData, 0)

        numNume = []
        for sample in spectrumData:
            numNume.append(sample - cero)
        
        denNum = np.arange(1, N, 1)
        denominador = np.sum(spectrumData)

        suma = 0
        for i in range(len(numNume)):
            divi = numNume[i]/denNum[i]
            suma += divi

        return suma / denominador