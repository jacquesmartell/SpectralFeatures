import soundfile as sf
from soundfile import SoundFile
import numpy as np

# CHECAR MAYOR LONGITUD DE TODOS LOS AUDIOS
def checkStems(inPaths):
    mayor = 0
    for path in inPaths:
        audio, sr = sf.read(path)
        if len(audio) > mayor:
            mayor = len(audio)
    return mayor


# LOAD AUDIOS
def loadAudio(inPaths, inConfig):
    print("---------")
    print("Añadiendo tracks...")
    tracks = []
    sampleRates = []
    cont = 0
    #lenMayor = checkStems(inPaths)

    print(inPaths)
    print(inConfig)

    '''for path in inPaths:
        audio = SoundFile(path.text())

        if audio.channels == 1:
            stereoSamples = []
            samples = audio.read()

            for i in range(lenMayor):
                if i >= len(samples):
                    stereoSample = [0.0, 0.0]
                else:
                    stereoSample = [samples[i], samples[i]]

                stereoSamples.append(stereoSample)

            stereoSound = np.append([[0.0, 0.0]], stereoSamples, axis=0)
            stereoSound = np.delete(stereoSound, 0, 0)
            tracks.append(stereoSound)
            samp, sr = sf.read(path.text())
            sampleRates.append(sr)

        else:
            stereoSamples = []
            samples = audio.read()
            for i in range(lenMayor):
                if i >= len(samples):
                    stereoSample = [0.0, 0.0]
                else:
                    stereoSample = [samples[i][0], samples[i][1]]

                stereoSamples.append(stereoSample)

            stereoSound = np.append([[0.0, 0.0]], stereoSamples, axis=0)
            stereoSound = np.delete(stereoSound, 0, 0)
            tracks.append(stereoSound)
            samp, sr = sf.read(path.text())
            sampleRates.append(sr)

        cont += 1'''

    return 0, 0