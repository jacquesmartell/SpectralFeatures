import numpy as np

def getRMS(inAudio, unit="db"):
    audio = np.array(inAudio)
    rms = np.sqrt(np.mean(audio**2))

    if unit == "dB":
        decibels = convertToDecibel(rms)
        return decibels
    elif unit == "linear":
        return rms

def convertToDecibel(inAudio):
    ref = 1
    if inAudio != 0:
        return 20 * np.log10(abs(inAudio) / ref)
    else:
        return -60