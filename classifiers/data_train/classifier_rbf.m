clc
clearvars -except X_train y_train X_test y_test
% create classifer model
Y_train = y_train + 1;
Y_test = y_test + 1;
feature = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 22 23];
% feature = [1:23];

%%% Create and Train RBF Network
% Set 'm' to the number of data points.
m = size(X_train(:,feature), 1);
% Train the RBFN using 5 centers
[Centers, betas, Theta] = trainRBFN(X_train(:,feature), Y_train, 5, true);

%%% Evaluate RBF classifer on Test Samples
% For each test sample...
n = size(X_test(:,feature), 1);

for (i = 1 : n)
    % Compute the scores for both categories.
    scores = evaluateRBFN(Centers, betas, Theta, X_test(i, feature));
	[maxScore, category(i)] = max(scores);	
end

cmat = confusionmat(Y_test,category')
run R1_clas.m
%% compute classifier resubstitution and cross validation error
clc
clearvars -except X_train y_train X_test y_test
Y_train = y_train + 1;
Y_test = y_test + 1;

indices = crossvalind('Kfold',Y_train,5);
cp = classperf(Y_train);
% feature = [1:23];
feature = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 22 23];
% feature = [1 10];
error_rate = 0;
for jj = 1:5
    for i = 1:5
        test = (indices == i); train = ~test;
        x_train_cv = X_train(train,feature);
        x_test_cv = X_train(test,feature);
        y_train_cv = Y_train(train,:);
        y_test_cv = Y_train(test,:);
        m = size(x_train_cv, 1);
        [Centers, betas, Theta] = trainRBFN(x_train_cv, y_train_cv, 5, true);
        n = size(x_test_cv, 1);
%         x_test = X_train(test,feature);
        category = [];
        for (ii = 1 : n)
            % Compute the scores for both categories.
            scores = evaluateRBFN(Centers, betas, Theta, x_test_cv(ii,:));
            [maxScore, category(ii)] = max(scores);	
        end
        class = category';
        classperf(cp,class,test);
    end
    error_rate = error_rate + cp.ErrorRate;
end
error_rate/5