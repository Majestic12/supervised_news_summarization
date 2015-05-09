clc
clearvars -except X_train y_train X_test y_test
% create classifer model
% feature = [1:23];
% feature = [1 2 3 4 8 12 13 14 17 18 20 21 22];
% feature = [1 10];
feature = [1 7 8];
options.MaxIter = 100000;
svm_struct = svmtrain(X_train(:,feature),y_train,'options',options);

% test classifier
class = svmclassify(svm_struct,X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m

%% compute classifier resubstitution and cross validation error
clc
clearvars -except X_train y_train X_test y_test
indices = crossvalind('Kfold',y_train,5);
cp = classperf(y_train);
% feature = [1:23];
% feature = [1 2 3 4 8 12 13 14 17 18 20 21 22];
% feature = [1 10];
feature = [3 4];

options.MaxIter = 100000;
error_rate = 0;
for jj = 1:3 
    for i = 1:5
        test = (indices == i); train = ~test;
        svm_struct = svmtrain(X_train(train,feature),y_train(train,:),'options',options);
        class = svmclassify(svm_struct,X_train(test,feature));
        classperf(cp,class,test);
    end
    error_rate = error_rate + cp.ErrorRate;
end
error_rate/3


