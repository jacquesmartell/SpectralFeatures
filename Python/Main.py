import Utilities.LoadAudio as load
import Descriptors.Centroid as centroid
import Descriptors.RMS as rms

track, sr = load.loadAudio("SpectralFeatures/Python/Tracks/kick.wav", inConfig="mono")

print(centroid.getCentroid(track, sr))

## dB or linear
print(rms.getRMS(track, unit="dB"))