clear all
load('FeatureLevel01.mat', 'F')
Training0 = F(1:2:end,1:32);% Training data before PCA-based feature selection
Testing0 = F(2:2:end,1:32);% Testing data before PCA-based feature selection
[U,S,V] = svd(Training0);

%% Scree plot
J = zeros(1,32);
for L = 1:32
    for k = (L+1):32
        J(L) = J(L)+S(k,k)^2;
    end
end
figure
plot(1:32,J,'-o')
xlabel('num PCs')
ylabel('sum of discarded eigenvalues')

%% Fraction of variance
total = 0;
for k = 1:32
    total = total+S(k,k)^2;
end
F = zeros(1,32);
for L = 1:32
    for k = 1:L
        F(L) = F(L)+S(k,k)^2;
    end
end
F = F/total;
figure
plot(1:32,F,'-o')
xlabel('num PCs')
ylabel('proportion of variance explained')