%% Spectral rolloff
function [rolloff] = spectralRolloff(audio, treshold)
% Spectrum
[xn, fs] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));
N = length(Xk);
k = linspace(0, fs/2, N);
k = k';

% Treshold
if ~exist('treshold', 'var')
    treshold = 0.95;
end

% Spectral rolloff
c = cumsum(Xk);
rolloff = k(find(c(:) >= c(end) * treshold, 1));