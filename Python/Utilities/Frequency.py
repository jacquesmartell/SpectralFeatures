from scipy.fft import rfftfreq;

def getFrequency(inSamples, inSampleRate):
    return(rfftfreq(len(inSamples), 1 / inSampleRate))