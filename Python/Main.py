import Utilities.LoadAudio as load
import Descriptors.Centroid as centroid
import Descriptors.RMS as rms
import Descriptors.Spread as spread
import Descriptors.Peak as peak
import Descriptors.Kurtosis as kurtosis
import Descriptors.RollOff as rolloff

track, sr = load.loadAudio("SpectralFeatures/Python/Tracks/Kick_1.wav", inConfig="mono")

# SELECT "Time" or "Frequency"
print("----------------")
print("Centroid in Time:", centroid.getCentroid(track, sr, inDomain="Time"))
print("Centroid in Frequency:", centroid.getCentroid(track, sr, inDomain="Frequency"))

# SELECT "dB" or "linear"
print("----------------")
print("RMS:", rms.getRMS(track, unit="linear"))

# SELECT "Time" or "Frequency"
print("----------------")
print("Spread in Time:", spread.getSpread(track, sr, inDomain="Time"))
print("Spread in Frequency:", spread.getSpread(track, sr, inDomain="Frequency"))

# SELECT "Time" or "Frequency"
print("----------------")
print("Peak in Time:", peak.getPeak(track, sr, inDomain="Time"))
print("Peak in Frequency:", peak.getPeak(track, sr, inDomain="Frequency"))

# SELECT "Time" or "Frequency"
print("----------------")
print("Kurtosis in Time:", kurtosis.getKurtosis(track, sr, inDomain="Time"))
print("Kurtosis in Frequency:", kurtosis.getKurtosis(track, sr, inDomain="Frequency"))

# SELECT "Time" or "Frequency"
print("----------------")
print("RollOff in Time:", rolloff.getRollOff(track, sr, inDomain="Time", threshold=0.95))
print("RollOff in Frequency:", rolloff.getRollOff(track, sr, inDomain="Frequency", threshold=0.95))