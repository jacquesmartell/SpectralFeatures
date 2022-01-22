%% Spectral decrease
function [decrease] = Decrease(audio)
% Spectrum
[xn, ~] = audioread(audio);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Spectral decrease
decrease = sum((Xk(2:end)-Xk(1)) ./ (1 : length(Xk)-1)') ./ sum(Xk(2:end));