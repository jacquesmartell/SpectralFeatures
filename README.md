# Spectral Features
Spectral features extraction for audio analysis.

## Included descriptors:

### Statistical features

| Feature            | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| Energy             | Sum of the squared amplitude of the signal.                  |
| Power              | Sum of the squared amplitude over one period of the signal.  |
| Root-mean-square   | Sum of the absolute value of the amplitude over one period of the signal. |
| Zero–crossing rate | Average rate of change of the signal’s sign.                 |



### Spectral shape features

| Feature           | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| Spectral centroid | Energetic center of the signal.                              |
| Spectral spread   | Deviation of the energy of the signal with respect to the centroid. |
| Spectral skewness | Lateral localization of the energy of the signal.            |
| Spectral kurtosis | Weigthed presence of the outliers in the signal’s tails.     |
| Spectral rolloff  | Estimation of the cutoff frequency of the signal.            |
| Spectral decrease | Average drop of the signal’s energy.                         |
| Spectral slope    | Degree of the steepness of the signal.                       |
| Spectral peak     | Frequency with highest energy concentration within the signal. |
| Spectral crest    | Ratio of the spectral peak to the signal’s mean.             |
| Spectral entropy  | White noise percentage of the signal.                        |
| Spectral flatness | Ratio of the signal’s geometric mean to its arithmetic mean. |
