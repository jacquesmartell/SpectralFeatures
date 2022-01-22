%% Spectral kurtosis
function [kurtosis] = Kurtosis(audio)
% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

% Spectral centroid
centroid = sum(Xk .* k) ./ sum(Xk);

% Spectral spread
spread = sqrt(sum((k - centroid).^2 .* Xk) ./ sum(Xk));

% Spectral kurtosis
kurtosis = sum((k - centroid).^4 .* Xk) ./ (spread^4 .* sum(Xk)) - 3;