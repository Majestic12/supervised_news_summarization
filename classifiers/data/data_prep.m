%%%
clear all
raw_data = importdata('rawdata.mat');
% initiate feataure vectors; variable X
temp1 = raw_data(:,1)./raw_data(:,2);
temp2 = raw_data(:,3)./raw_data(:,4);
X = [raw_data(:,1) temp1 raw_data(:,3) temp2 raw_data(:,5:22)];
clear temp1 temp2

%%% feature normalization; update X
% feature scaling
epsilon = 0.1;
X = ((1 - 2*epsilon)*(X-repmat(min(X),length(X),1))./(repmat(max(X),length(X),1)-repmat(min(X),length(X),1))) + epsilon;
clear epsilon

%%% create class vector; varabile Y
Y = raw_data(:,24);
clear raw_data

%%
%%% randomly select equal number of true and false class; update X & Y
% select all TRUE class (b/c too few of them)
index_1 = find(Y); %return index of TRUE class
X_1 = X(index_1,:);
% randomly select equal # of FALSE class (as TRUE class)
index_0 = find(Y==0);
X_0 = X(index_0,:);
X_0_scaled = X_0(randsample(length(X_0),length(X_1)),:);

X = [X_0_scaled; X_1];
Y = [zeros(length(X_0_scaled),1); ones(length(X_1),1)];
clear index_0 index_1 X_0 X_0_scaled X_1



