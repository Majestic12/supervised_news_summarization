clc
% create classifer model
% for j = 1:22
feature = [3:5 9:13 17 19 21];
% feature = [j];

mdl = fitNaiveBayes(X(:,feature),Y);
class = mdl.predict(X(:,feature));
cmat = confusionmat(Y,class)

% compute classifier resubstitution and cross validation error using
% (training + validation data)

avg_kfold = 0;

for i = 1:20
    c = cvpartition(Y,'kFold',5);
    fun = @(xT,yT,xt,yt)(sum(~strcmp(yt,classify(xt,xT,yT))));
    rate = sum(crossval(fun,X(:,feature),Y,'partition',c))...
           /sum(c.TestSize);
    avg_kfold = avg_kfold + rate;
end
% j

avg_kfold/20

% end

