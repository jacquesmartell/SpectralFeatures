%% Spectral entropy
function [entropy] = spectralEntropy(audio)
% Spectrum
[xn, ~] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);

% Spectral entropy
X = Xk ./ sum(Xk);
entropy = -sum(X .* log(X)) ./ log(N);
fprintf('Entropy: %f\n', entropy)