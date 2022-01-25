%% Spectral flatness
function [flatness] = spectralFlatness(audio)
% Spectrum
[xn, ~] = audioread(audio);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Spectral flatness
flatness = exp(mean(log(Xk))) ./ mean(Xk);