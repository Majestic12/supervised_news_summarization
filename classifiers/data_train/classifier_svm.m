clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1 2 3 4 8 12 13 14 17 18 20 21 22];
options.MaxIter = 100000;
svm_struct = svmtrain(X_train(:,feature),y_train,'options',options);

% test classifier
class = svmclassify(svm_struct,X_test(:,feature));
cmat = confusionmat(y_test,class);

run R1_clas.m

% compute classifier resubstitution and cross validation error




