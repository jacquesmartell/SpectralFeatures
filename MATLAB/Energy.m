%% Energy
function [energy] = Energy(audio)
% Spectrum
[xn, ~] = audioread(audio);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Energy
energy = sum(Xk.^2);