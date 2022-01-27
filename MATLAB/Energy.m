%% Energy
function [energy] = Energy(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Energy
energy = sum(Xk.^2);