%% Spectral slope
function [slope] = spectralSlope(audio)
% Spectrum
[xn, fs] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));
N = length(Xk);
k = linspace(0, fs/2, N);
k = k';

% Spectral slope
slope = sum((k - mean(k)) .* (Xk - mean(Xk))) ./ sum((k - mean(k)).^2);