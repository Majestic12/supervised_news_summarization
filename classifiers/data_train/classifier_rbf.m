clc
clearvars -except X Y
% create classifer model
feature = [3:5 9:13 17 19 21];

% updated training and testing data, X & Y
X_train = X(:,feature);
y_train = 1 + Y;

X_test = X_train;
y_test = y_train;

%% Create and Train RBF Network
% Set 'm' to the number of data points.
m = size(X_train, 1);

% Train the RBFN using 5 centers
[Centers, betas, Theta] = trainRBFN(X_train, y_train, 5, true);
 

%% Evaluate RBF classifer on Test Samples
% compute classifier resubstitution and cross validation error using
% (training + validation data)
% For each test sample...
n = size(X_test, 1);
numRight = 0;
wrong = [];
for (i = 1 : n)
    % Compute the scores for both categories.
    scores = evaluateRBFN(Centers, betas, Theta, X_test(i, :));
	[maxScore, category(i)] = max(scores);	
end

R2 = confusionmat(y_test,category')
error = (sum(sum(R2))-sum(diag(R2)))/sum(sum(R2))

