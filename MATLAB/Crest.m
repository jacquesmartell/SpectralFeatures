%% Spectral crest
function [crest] = Crest(audio)
% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

% Spectral peak
[~, iMax] = max(Xk);
peak = k(iMax);

% Spectral crest
crest = peak / mean(Xk);