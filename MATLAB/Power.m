%% Power
function [power] = Power(audio)
% Spectrum
[xn, ~] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Power
power = sum(Xk.^2) / (2*N + 1);