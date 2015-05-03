clc
% create classifer model
feature = [3:5 9:13 17 19 21];

% updated training and testing data, X & Y
X_train = X(:,feature);
y_train = Y;

X_test = X_train;
y_test = y_train;

%RVM w/ Linear Kernel
% rvm_mdl = rvmFit(X_train, y_train, 'kernelFn', @kernelLinear);

%RVM w/ Polynomial Kernel
d = 5;
rvm_mdl = rvmFit(X_train, y_train, 'kernelFn', @(X1, X2)kernelPoly(X1, X2, d));

%RVM w/ Gaussian Kernel
% sigma = mean(var(X_train).^2);
% sigma = 0.05; %manually set sigma
% rvm_mdl = rvmFit(X_train,y_train, 'kernelFn', @(X1, X2)kernelRbfSigma(X1, X2, sigma));


% compute classifier resubstitution and cross validation error using
% (training + validation data)
mdl_pred = rvmPredict(rvm_mdl,X_test);
R2 = confusionmat(y_test,mdl_pred)
error = (sum(sum(R2))-sum(diag(R2)))/sum(sum(R2))



