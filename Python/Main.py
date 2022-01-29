import Utilities.LoadAudio as load
import Descriptors.Centroid as centroid

track, sr = load.loadAudio("SpectralFeatures/Python/Tracks/kick.wav", inConfig="mono")

print(centroid.getCentroid(track, sr))