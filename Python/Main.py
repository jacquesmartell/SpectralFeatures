import Utilities.LoadAudio as load
import Descriptors.Centroid as centroid

samples, sr = load.loadAudio("Tracks/Pad.wav", "mono")

centroid.getCentroid(samples, sr)