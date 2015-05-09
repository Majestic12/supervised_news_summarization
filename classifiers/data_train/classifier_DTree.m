clc
clearvars -except X_train y_train X_test y_test
% create classifer model
feature = [1:23];
DT_mdl = fitctree(X_train(:,feature),y_train);
% view(DT_mdl,'Mode','graph')
    
% test classifier
class = DT_mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m


%% compute classifier resubstitution and cross validation error
avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(DT_mdl);

    DT_mdl_CV = crossval(DT_mdl,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(DT_mdl_CV);
end
avg_resub/20;
1-avg_kfold/20
