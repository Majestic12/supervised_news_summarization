clc
clearvars -except X_train y_train X_test y_test
% create classifer model
% feature = [1:23];
% feature = [1:6 10:12 14 23];
feature = [1 7 11 15];
% feature = [1 10];
mdl = fitNaiveBayes(X_train(:,feature),y_train);

% test classifier
class = mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m
% compute classifier resubstitution and cross validation error 


%%
clc
clearvars -except X_train y_train X_test y_test
indices = crossvalind('Kfold',y_train,5);
cp = classperf(y_train);
% feature = [1:23];
% feature = [1 2 3 4 5 6 10 11 12 14 23];
feature = [1 6 12 15 18];
% feature = [1 10];

error_rate = 0;
for jj = 1:20 
    for i = 1:5
        test = (indices == i); train = ~test;
        mdl = fitNaiveBayes(X_train(train,feature),y_train(train,:));
        class = mdl.predict(X_train(test,feature));
        classperf(cp,class,test);
    end
    error_rate = error_rate + cp.ErrorRate;
end
error_rate/20
