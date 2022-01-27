# Spectral Features
Statistical and spectral features extraction for audio analysis.

<br>



### Statistical features

Obtained using the time domain.

| Feature            | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| Energy             | Sum of the squared amplitude of the signal.                  |
| Power              | Sum of the squared amplitude over one period of the signal.  |
| Root-mean-square   | Sum of the absolute value of the amplitude over one period of the signal. |
| Zero–crossing rate | Average rate of change of the signal’s sign.                 |

<br>



### Spectral shape features

Obtained using the frequency domain

| Feature           | Description                                                  | Formula                                                      |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Spectral centroid | Energetic center of the signal.                              | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mu_1=\dfrac{\sum_{k=0}^N\|X_k\|\, k}{\sum_{k=0}^N\|X_k\|}"> |
| Spectral spread   | Deviation of the energy of the signal with respect to the centroid. | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mu_2=\sqrt{\dfrac{\sum_{k=0}^N(k-\mu_1)^2\,\|X_k\|}{\sum_{k=0}^N\|X_k\|}}"> |
| Spectral skewness | Lateral localization of the energy of the signal.            | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mu_3=\dfrac{\sum_{k=0}^N(k-\mu_1)^3\,\|X_k\|}{\mu_2^3\,\sum_{k=0}^N\|X_k\|}"> |
| Spectral kurtosis | Weigthed presence of the outliers in the signal’s tails.     | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mu_4=\dfrac{\sum_{k=0}^N(k-\mu_1)^4\,\|X_k\|}{\mu_2^4\,\sum_{k=0}^N\|X_k\|}-3"> |
| Spectral rolloff  | Estimation of the cutoff frequency of the signal.            | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{R}=k\Bigg \|_{\sum_{k=0}^N\|X_k\|=\tau\sum_{k=0}^N\|X_k\|}"> |
| Spectral decrease | Average drop of the signal’s energy.                         | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{D}=\dfrac{\sum_{k=0}^N\frac{\|X_k\|-\|X_0\|}{N-1}}{\sum_{k=0}^N\|X_k\|}"> |
| Spectral slope    | Degree of the steepness of the signal.                       | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{S}=\dfrac{\sum_{k=0}^N(k-\bar{k})(\|X_k\|-\bar{\|X_k\|})}{\sum_{k=0}^N(k-\bar{k})^2}"> |
| Spectral peak     | Frequency with highest energy concentration within the signal. | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{P}=\max(\|X_k\|)"> |
| Spectral crest    | Ratio of the spectral peak to the signal’s mean.             | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{C}=\dfrac{\max(\|X_k\|)}{\bar{\|X_k\|}}"> |
| Spectral entropy  | White noise percentage of the signal.                        | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{E}=-\dfrac{\sum_{k=0}^N\tilde{\|X_k\|}\,\log(\tilde{\|X_k\|})}{\log(N)}"> |
| Spectral flatness | Ratio of the signal’s geometric mean to its arithmetic mean. | <img src="https://render.githubusercontent.com/render/math?math=\color{grey}\mathrm{F}=\dfrac{\sqrt[N]{\prod_{k=0}^N\|X_k\|}}{\frac{1}{N}\sum_{k=0}^N\|X_k\|}"> |
