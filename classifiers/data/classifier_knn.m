% create classifer model

% feature = [3:5 9:13 17 19 21];
% feature = [1:22];

knn_md1 = fitcknn(X(:,feature),Y,'NumNeighbors',5);

% compute classifier resubstitution and cross validation error using
% (training + validation data)

avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(knn_md1);

    knn_md1_CV = crossval(knn_md1,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(knn_md1_CV);
end

avg_resub/20
avg_kfold/20

