%% Zero-crossing rate
function [zcr] = ZeroCrossRate(audio)
% Spectrum
[xn, ~] = audioread(audio);

% Zero-crossing rate
zcr = mean(abs(diff(sign(xn))));
fprintf('Zero-crossing rate :%f\n', zcr)