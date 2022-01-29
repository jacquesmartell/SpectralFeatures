import librosa

def getMFCC(inSamples, inSampleRate, mfcc=13):
    resul = []
    mfccValue = librosa.feature.mfcc(inSamples, sr=inSampleRate, n_mfcc=mfcc)
    for mfcc in mfccValue:
        resul.append(mfcc.mean())
    
    return resul