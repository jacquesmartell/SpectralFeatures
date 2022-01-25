%% Spectral centroid
function [centroid] = spectralCentroid(audio)
% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

% Spectral centroid
centroid = sum(Xk .* k) ./ sum(Xk);