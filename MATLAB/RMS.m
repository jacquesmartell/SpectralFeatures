%% Root-mean-square
function [rms] = RMS(audio)
% Spectrum
[xn, ~] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% RMS
rms = sqrt(sum(Xk.^2) / N);