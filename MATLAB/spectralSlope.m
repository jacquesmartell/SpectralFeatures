%% Spectral slope
function [slope] = spectralSlope(audio)
% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

% Spectral slope
slope = sum((k - mean(k)) .* (Xk - mean(Xk))) ./ sum((k - mean(k)).^2);