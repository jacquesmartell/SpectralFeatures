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
import Descriptors.Skewness as skewness
import Descriptors.Slope as slope
import Descriptors.Crest as crest
import Descriptors.Flatness as flatness
import Descriptors.Decrease as decrease

# LOAD TRACK
#samples, sr = load.loadAudio("SpectralFeatures/Python/Tracks/Kick_1.wav", inConfig="mono")

samples = [0.5, 0.3, 0.2, 0.6, -0.2, -0.7, 0.20, 0.47, -0.21, 0.99]
sr = 48000

### RMS ###
# SELECT "dB" or "linear"
print("----------------")
print("RMS:", rms.getRMS(samples, unit="linear"))
print("RMS:", rms.getRMS(samples, unit="dB"))

### Centroid ###
print("----------------")
print("Centroid in Time:", centroid.getCentroid(samples, sr, inDomain="Time"))
print("Centroid in Frequency:", centroid.getCentroid(samples, sr, inDomain="Frequency"))

### Peak ###
print("----------------")
print("Peak in Time:", peak.getPeak(samples, sr, inDomain="Time"))
print("Peak in Frequency:", peak.getPeak(samples, sr, inDomain="Frequency"))

### Spread ###
print("----------------")
print("Spread in Time:", spread.getSpread(samples, sr, inDomain="Time"))
print("Spread in Frequency:", spread.getSpread(samples, sr, inDomain="Frequency"))

### Kurtosis ###
print("----------------")
print("Kurtosis in Time:", kurtosis.getKurtosis(samples, sr, inDomain="Time"))
print("Kurtosis in Frequency:", kurtosis.getKurtosis(samples, sr, inDomain="Frequency"))

### RollOff ###
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

### SKEWNESS ###
print("----------------")
print("Skewness in Time:", skewness.getSkewness(samples, sr, inDomain="Time"))
print("Skewness in Frequency:", skewness.getSkewness(samples, sr, inDomain="Frequency"))

### SLOPE ###
print("----------------")
print("Slope in Time:", slope.getSlope(samples, sr, inDomain="Time"))
print("Slope in Frequency:", slope.getSlope(samples, sr, inDomain="Frequency"))

### CREST ###
print("----------------")
print("Crest in Time:", crest.getCrest(samples, sr, inDomain="Time"))
print("Crest in Frequency:", crest.getCrest(samples, sr, inDomain="Frequency"))

### FLATNESS ###
print("----------------")
print("Flatness:", flatness.getFlatness(samples, sr))

### DECREASE ###
print("----------------")
print("Decrease in Time:", decrease.getDecrease(samples, sr, inDomain="Time"))
print("Decrease in Frequency:", decrease.getDecrease(samples, sr, inDomain="Frequency"))