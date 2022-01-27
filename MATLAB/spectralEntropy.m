%% Spectral entropy
function [entropy] = spectralEntropy(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);
Xk = abs(fft(xn));
Xk = Xk(1 : round(end/2));
N = length(Xk);

% Spectral entropy
X = Xk ./ sum(Xk);
entropy = -sum(X .* log(X)) ./ log(N);
fprintf('Entropy: %f\n', entropy)