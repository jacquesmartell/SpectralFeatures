%% Spectral decrease
function [decrease] = spectralDecrease(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));

% Spectral decrease
decrease = sum((Xk(2:end)-Xk(1)) ./ (1 : length(Xk)-1)') ./ sum(Xk(2:end));