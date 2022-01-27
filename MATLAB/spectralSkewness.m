%% Spectral skewness
function [skewness] = spectralSkewness(audio)
% Spectrum
[xn, fs] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));
N = length(Xk);
k = linspace(0, fs/2, N);
k = k';

% Spectral centroid
centroid = sum(Xk .* k) ./ sum(Xk);

% Spectral spread
spread = sqrt(sum((k - centroid).^2 .* Xk) ./ sum(Xk));

% Spectral skewness
skewness = sum((k - centroid).^3 .* Xk) ./ (spread^3 .* sum(Xk));