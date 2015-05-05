clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1 2 3 4 9 10 11 12 13 15 16 17 18 20 22 23];
qda_mdl = fitcdiscr(X_train(:,feature),y_train,'DiscrimType','quadratic');

% test classifier
class = qda_mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m
%%
% compute classifier resubstitution and cross validation error
avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(qda_mdl);

    qda_mdl_CV = crossval(qda_mdl,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(qda_mdl_CV);
end
avg_resub/20;
1-avg_kfold/20

