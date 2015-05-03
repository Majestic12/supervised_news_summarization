clc

% redefine class Y
Ytrain = 1+Y;

% create classifer model
feature = [3:5 9:13 17 19 21];
svm_struct = svmtrain(X(:,feature),Ytrain);

% compute classifier resubstitution and cross validation error using
% (training + validation data)

YtestHat = svmclassify(svm_struct,X(:,feature)); %tested on trained sample!
%Correct Classification Rate (CCR)
CCR = trace(confusionmat(Ytrain,YtestHat))/sum(sum(confusionmat(Ytrain,YtestHat)))



