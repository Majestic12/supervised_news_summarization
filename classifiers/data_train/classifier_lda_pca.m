% Training and Testing data
feature = [1:22];
X_train = X([1:60 122:181],feature);
y_train = Y([1:60 122:181],:);
X_test = X([61:121 182:242],feature);
y_test = Y([61:121 182:242],:);

[U,S,V] = svd(X_train);
NumPCA = 22; %number of principal component to be used
C = zeros(2,2,NumPCA); %confusion matrices
ErrorRate = zeros(1,NumPCA); %error rates

for ii = 1:NumPCA
    Train = X_train*V(:,1:ii); %training data
    Test = X_test*V(:,1:ii); %testing data
    % create classifer model
    lda_mdl = fitcdiscr(X_train,y_train);
    Y_testHat = predict(lda_mdl,X_test);
    C(:,:,ii) = confusionmat(y_test,Y_testHat);
    ErrorRate(ii) = 1-trace(C(:,:,ii))/sum(sum(C(:,:,ii)));
end

% plot error rate vs number of principal components
plot(1:NumPCA,ErrorRate,'-o')
xlabel('Number of Principal Components')
ylabel('Error Rate')






