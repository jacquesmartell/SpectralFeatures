%% Spectral rolloff
function [rolloff] = spectralRolloff(audio, treshold)
% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

% Treshold
if ~exist('treshold', 'var')
    treshold = 0.95;
end

% Spectral rolloff
c = cumsum(Xk);
rolloff = k(find(c(:) >= c(end) * treshold, 1));