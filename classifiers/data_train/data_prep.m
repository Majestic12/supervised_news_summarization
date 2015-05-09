%%%
% raw_data = importdata('rawdata.mat');
raw_data = importdata('data_test_econ.mat');

%%% Data clean-up
% keep sentences with 3 < word-length < 50
ind_wl = find(raw_data(:,5) > 3 & raw_data(:,5) <= 50);
raw_data = raw_data(ind_wl,:);

% exclude sentences that are tagged as quote
ind_q = find(raw_data(:,6)==0);
raw_data = raw_data(ind_q,:);
clear ind_wl ind_q

% initiate feataure vectors; X
temp1 = raw_data(:,1)./raw_data(:,2);
temp2 = raw_data(:,3)./raw_data(:,4);
X = [raw_data(:,1:2) temp1 raw_data(:,3:4) temp2 raw_data(:,[5 7:22])];
clear temp1 temp2

%%% feature normalization; update X
% feature scaling
epsilon = 0.1;
% X_min = min(X);
X_min = [1 3 0.0066 1 1 0.0233 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1];
% X_max = max(X);
X_max = [151 151 1 43 43 1 50 15 8 9 7 10 26 33 13 9 7 11 5 17 10 16 36];
X = ((1 - 2*epsilon)*(X-repmat(X_min,length(X),1))./(repmat(X_max,length(X),1)-repmat(X_min,length(X),1))) + epsilon;
clear epsilon

%%% create class vector; Y
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
X_0_sel = X_0(randsample(length(X_0),length(X_1)),:);


%%% create training or testing feature vectors; X_train or X_test
X_test = [X_0_sel; X_1];
%%% create training or testing class vector; y_train or y_test
y_test = [zeros(length(X_0_sel),1); ones(length(X_1),1)];
clear index_0 index_1 X_0 X_0_sel X_1 X Y X_min X_max



