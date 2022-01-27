%% Spectral crest
function [crest] = spectralCrest(audio)
% Spectrum
[xn, fs] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));
N = length(Xk);
k = linspace(0, fs/2, N);
k = k';

% Spectral peak
[~, iMax] = max(Xk);
peak = k(iMax);

% Spectral crest
crest = peak / mean(Xk);