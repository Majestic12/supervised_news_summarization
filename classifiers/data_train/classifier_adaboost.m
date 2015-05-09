clc
clearvars -except X_train y_train X_test y_test
% create classifer model
% feature = [1 10];
feature = [1 3 10 16 18 23];
Y_train = y_train;
Y_test = y_test;
ada_mdl = fitensemble(X_train(:,feature),Y_train,'AdaBoostM1',100,'Tree');

% test classifier
class = predict(ada_mdl,X_test(:,feature)); 
cmat = confusionmat(y_test,class)
run R1_clas.m

%% compute classifier resubstitution and cross validation error
clc
clearvars -except X_train y_train X_test y_test
indices = crossvalind('Kfold',y_train,5);
cp = classperf(y_train);
% feature = [1:23];
feature = [1 3 10 16 18 23];
% feature = [1 10];

error_rate = 0;
for jj = 1:3 
    for i = 1:5
        test = (indices == i); train = ~test;
        mdl = fitensemble(X_train(train,feature),y_train(train,:),'AdaBoostM1',100,'Tree');
        class = predict(mdl,X_train(test,feature));
        classperf(cp,class,test);
    end
    error_rate = error_rate + cp.ErrorRate;
end
error_rate/3


