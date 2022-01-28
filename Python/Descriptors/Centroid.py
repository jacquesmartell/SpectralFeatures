import numpy as np
import Utilities.Amplitude as amplitude
import Utilities.Frequency as frequency

def getCentroid(inSamples, inSampleRate):
    amplitudeData = amplitude.getAmplitude(inSamples)
    frequencyData = frequency.getFrequency(inSamples, inSampleRate)
    return np.sum(amplitudeData * frequencyData) / np.sum(amplitudeData)