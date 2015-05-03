clc
% create classifer model
for j = 1:22
% feature = [3:5 9:13 17 19 21];
feature = [j];

lda_md1 = fitcdiscr(X(:,feature),Y);

% compute classifier resubstitution and cross validation error using
% (training + validation data)

avg_resub = 0;
avg_kfold = 0;
for i = 1:20
    avg_resub = avg_resub + resubLoss(lda_md1);

    lda_md1_CV = crossval(lda_md1,'kfold',5);
    avg_kfold = avg_kfold + kfoldLoss(lda_md1_CV);
end
j
avg_resub/20;
avg_kfold/20
end

