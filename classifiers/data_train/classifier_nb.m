clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1 2 3 4 5 6 10 11 12 14 23];
mdl = fitNaiveBayes(X_train(:,feature),y_train);

% test classifier
class = mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m
% compute classifier resubstitution and cross validation error 


