clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1 2 3 9 11];
% feature = [3 4 11 13 17 20];
% feature = [1 10];
%RVM w/ Linear Kernel
% rvm_mdl = rvmFit(X_train(:,feature), y_train, 'kernelFn', @kernelLinear);

%RVM w/ Polynomial Kernel
d = 2;
rvm_mdl = rvmFit(X_train(:,feature), y_train, 'kernelFn', @(X1, X2)kernelPoly(X1, X2, d));

%RVM w/ Gaussian Kernel
% % sigma = mean(var(X_train).^2);
% sigma = 0.6; %manually set sigma
% rvm_mdl = rvmFit(X_train(:,feature),y_train, 'kernelFn', @(X1, X2)kernelRbfSigma(X1, X2, sigma));

% test classifier
class = rvmPredict(rvm_mdl,X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m

%% compute classifier resubstitution and cross validation error
clc
clearvars -except X_train y_train X_test y_test
% feature = [1 2 3 9 11];
feature = [3 4 11 13 17 20];
% feature = [1 2 3 4];
% feature = [1:23];

indices = crossvalind('Kfold',y_train,5);
cp = classperf(y_train);

d = 3;
sigma = 0.6;
error_rate = 0;
for jj = 1:5 
    for i = 1:5
        test = (indices == i); train = ~test;
%         mdl = rvmFit(X_train(train,feature),y_train(train,:), 'kernelFn', @kernelLinear);                           %linear
        mdl = rvmFit(X_train(train,feature),y_train(train,:), 'kernelFn', @(X1, X2)kernelPoly(X1, X2, d));          %poly
%         mdl = rvmFit(X_train(train,feature),y_train(train,:), 'kernelFn', @(X1, X2)kernelRbfSigma(X1, X2, sigma));  %rbf
        class = rvmPredict(mdl,X_train(test,feature));
        classperf(cp,class,test);
    end
    error_rate = error_rate + cp.ErrorRate;
end
error_rate/5


