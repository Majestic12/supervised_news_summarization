clear all
close all
%%%
raw_data = importdata('rawdata.mat');
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

% %%% feature normalization; update X
% % feature scaling
% epsilon = 0.1;
% % X_min = min(X);
% X_min = [1 3 0.0066 1 1 0.0233 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1];
% % X_max = max(X);
% X_max = [151 151 1 43 43 1 50 15 8 9 7 10 26 33 13 9 7 11 5 17 10 16 36];
% X = ((1 - 2*epsilon)*(X-repmat(X_min,length(X),1))./(repmat(X_max,length(X),1)-repmat(X_min,length(X),1))) + epsilon;
% clear epsilon

%%% create class vector; Y
Y = raw_data(:,24);
clear raw_data
%%
%%%
% create X and Y training data
X_train = X;
y_train = Y;
clear X Y X_max X_min
ind_t = find(y_train); % index of true class
ind_f = find(~y_train);% index of false class
%%
% visualize data
f1 = X_train(:,3);
f10 = X_train(:,10);
gscatter(f1,f10,y_train,'rb');
legend('False','True')
%% histogram overlap
hist(X_train(ind_f,1),200)
hold on
hist(X_train(ind_t,1),200)
h = findobj(gca,'type','patch');
set(h(1),'Facecolor',[0,0,1],'EdgeColor','k');
set(h(2),'Facecolor',[1,0,0],'EdgeColor','k');
%% histogram as subplots
i = 3;
subplot(2,1,1); hist(X_train(ind_t,i),180);
h = findobj(gca,'type','patch');
set(h,'Facecolor',[0,0,1],'EdgeColor','k');
subplot(2,1,2); hist(X_train(ind_f,i),180);
h = findobj(gca,'type','patch');
set(h,'Facecolor',[1,0,0],'EdgeColor','k');
