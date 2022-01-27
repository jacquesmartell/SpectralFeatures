%% Zero-crossing rate
function [zcr] = ZeroCrossRate(audio)
% Spectrum
[xn, ~] = audioread(audio);
xn = (xn(:, 1) + xn(:, 2)) / size(xn, 2);

% Zero-crossing rate
zcr = mean(abs(diff(sign(xn))));
fprintf('Zero-crossing rate :%f\n', zcr)