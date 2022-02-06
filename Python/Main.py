import Utilities.LoadAudio as load
import Descriptors.Centroid as centroid
import Descriptors.RMS as rms
import Descriptors.Spread as spread
import Descriptors.Peak as peak
import Descriptors.Kurtosis as kurtosis
import Descriptors.RollOff as rolloff
import Descriptors.Entropy as entropy
import Descriptors.MFCC as mfcc
import Descriptors.Energy as energy
import Descriptors.Power as power
import Descriptors.ZeroCrossing as zerocrossing

# LOAD TRACK
samples, sr = load.loadAudio("SpectralFeatures/Python/Tracks/Guitar_1.wav", inConfig="mono")

#samples = [0.5, 0.3, 0.2, 0.6, -0.2, -0.7, 0.20, 0.47, -0.21, 0.99]
#sr = 48000

### RMS ###
# SELECT "dB" or "linear"
print("----------------")
print("RMS:", rms.getRMS(samples, unit="linear"))
print("RMS:", rms.getRMS(samples, unit="dB"))

### Centroid ###
# SELECT "Time" or "Frequency"
print("----------------")
print("Centroid in Time:", centroid.getCentroid(samples, sr, inDomain="Time"))
print("Centroid in Frequency:", centroid.getCentroid(samples, sr, inDomain="Frequency"))

### Peak ###
# SELECT "Time" or "Frequency"
print("----------------")
print("Peak in Time:", peak.getPeak(samples, sr, inDomain="Time"))
print("Peak in Frequency:", peak.getPeak(samples, sr, inDomain="Frequency"))

### Spread ###
# SELECT "Time" or "Frequency"
print("----------------")
print("Spread in Time:", spread.getSpread(samples, sr, inDomain="Time"))
print("Spread in Frequency:", spread.getSpread(samples, sr, inDomain="Frequency"))

### Kurtosis ###
# SELECT "Time" or "Frequency"
print("----------------")
print("Kurtosis in Time:", kurtosis.getKurtosis(samples, sr, inDomain="Time"))
print("Kurtosis in Frequency:", kurtosis.getKurtosis(samples, sr, inDomain="Frequency"))

### RollOff ###
# SELECT "Time" or "Frequency"
print("----------------")
print("RollOff in Time:", rolloff.getRollOff(samples, sr, inDomain="Time"))
print("RollOff in Frequency:", rolloff.getRollOff(samples, sr, inDomain="Frequency"))

### Entropy ###
print("----------------")
print("Entropy in Time:", entropy.getEntropy(samples, sr, inDomain="Time"))
print("Entropy in Frequency:", entropy.getEntropy(samples, sr, inDomain="Frequency"))

### MFCC ###
print("----------------")
print("MFCC:", mfcc.getMFCC(samples, sr, mfcc=13))

### ENERGY ###
print("----------------")
print("Energy:", energy.getEnergy(samples, sr))

### POWER ###
print("----------------")
print("Power:", power.getPower(samples, sr))

### ZERO CROSSING ###
print("----------------")
print("Zero-Crossing:", zerocrossing.getZeroCrossing(samples, sr))