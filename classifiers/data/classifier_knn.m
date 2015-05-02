% create classifer model
knn_md1 = fitcknn(X,Y);

% compute classifier resubstitution and cross validation error using
% (training + validation data)

resubLoss(knn_md1)

knn_md1_CV = crossval(knn_md1,'kfold',5);
kfoldLoss(knn_md1_CV)

