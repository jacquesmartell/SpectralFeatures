%% Root-mean-square
function [rms] = RMS(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% RMS
rms = sqrt(sum(Xk.^2) / N);