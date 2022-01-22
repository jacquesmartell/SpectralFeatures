%% Spectral features
function SpectralFeatures(audio)

%% Spectrum
[xn, fs] = audioread(audio);
N = length(xn);
Xk = abs(fft(xn));
Xk = Xk(1 : end/2);
k = linspace(0, fs/2, N/2);
k = k';

%% Statistic descriptors
% Energy
energy = sum(Xk.^2);
fprintf('Energy: %f\n', energy)

% Power
power = sum(Xk.^2) / (2*N + 1);
fprintf('Power: %f\n', power)

% RMS
RMS = sqrt(sum(Xk.^2) / N);
fprintf('RMS: %f\n', RMS)

%% Spectral shape descriptors
% Spectral centroid
centroid = sum(Xk .* k) ./ sum(Xk);
fprintf('Centroid: %f\n', centroid)

% Spectral spread
spread = sqrt(sum((k - centroid).^2 .* Xk) ./ sum(Xk));
fprintf('Spread: %f\n', spread)

% Spectral skewness
skewness = sum((k - centroid).^3 .* Xk) ./ (spread^3 .* sum(Xk));
fprintf('Skewness: %f\n', skewness)

% Spectral kurtosis
kurtosis = sum((k - centroid).^4 .* Xk) ./ (spread^4 .* sum(Xk)) - 3;
fprintf('Kurtosis: %f\n', kurtosis)

% Spectral rolloff
c = cumsum(Xk);
rolloff = k(find(c(:) >= c(end) * 0.95, 1));
fprintf('Rolloff: %f\n', rolloff)

% Spectral decrease
decrease = sum((Xk(2:end)-Xk(1)) ./ (1 : length(Xk)-1)') ./ sum(Xk(2:end));
fprintf('Decrease: %f\n', decrease)

% Spectral slope
slope = sum((k - mean(k)) .* (Xk - mean(Xk))) ./ sum((k - mean(k)).^2);
fprintf('Slope: %f\n', slope)

%% Signal properties
% Spectral peak
[~, iMax] = max(Xk);
peak = k(iMax);
fprintf('Peak: %f\n', peak)

% Spectral crest
crest = peak / mean(Xk);
fprintf('Crest: %f\n', crest)

% Spectral flatness
flatness = exp(mean(log(Xk))) ./ mean(Xk);
fprintf('Flatness: %f\n', flatness)