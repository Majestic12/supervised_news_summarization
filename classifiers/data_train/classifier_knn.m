clearvars -except X_train y_train X_test y_test
% create classifer model
% feature = [1 10];
feature = [1 2 3 4 5 6 7 9 10 11 12 13 14 15 16 17 18 20 22 23];
% feature = [1 2 3 4 6 7 10 14 15];
knn_mdl = fitcknn(X_train(:,feature),y_train,'NumNeighbors',13);

% test classifier
class = knn_mdl.predict(X_test(:,feature));
cmat = confusionmat(y_test,class)
run R1_clas.m

%%
% compute classifier resubstitution and cross validation error
avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(knn_mdl);

    knn_mdl_CV = crossval(knn_mdl,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(knn_mdl_CV);
end
avg_resub/20;
avg_kfold/20

