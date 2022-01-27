%% Spectral flatness
function [flatness] = spectralFlatness(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));

% Spectral flatness
flatness = exp(mean(log(Xk))) ./ mean(Xk);