clc
% create classifer model
feature = [3:5 9:13 17 19 21];

DT_mdl = fitctree(X(:,feature),Y,'PredictorNames',...
    {'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K'});

% compute classifier resubstitution and cross validation error using
% (training + validation data)
avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(DT_mdl);

    DT_mdl_CV = crossval(DT_mdl,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(DT_mdl_CV);
end
avg_resub/20;
avg_kfold/20
