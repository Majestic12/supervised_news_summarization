clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1 2 3 4 6 7 10];
% feature = [1:23];
lda_mdl = fitcdiscr(X_train(:,feature),y_train);

% test classifier
class = lda_mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m
%%
% compute classifier resubstitution and cross validation error
avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(lda_mdl);

    lda_mdl_CV = crossval(lda_mdl,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(lda_mdl_CV);
end
avg_resub/20;
avg_kfold/20


