clc
% training and testing data
feature = [3:5 9:13 17 19 21];
X_train = X(:,feature);
y_train = 1+Y;
X_test = X_train; %?!
y_test = y_train;


% create classifer model
ada_mdl = fitensemble(X_train,y_train,'AdaBoostM1',100,'Tree');

% compute classifier resubstitution and cross validation error using
% (training + validation data)
YtestHat = predict(ada_mdl,X_test); %tested on trained sample!

%Correct Classification Rate (CCR)
R2 = confusionmat(y_test,YtestHat)
CCR = trace(R2)/sum(sum(R2))



