%% Spectral skewness
function [skewness] = Skewness(audio)
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

% Spectral skewness
skewness = sum((k - centroid).^3 .* Xk) ./ (spread^3 .* sum(Xk));