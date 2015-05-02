%%% 
% create one matrix will all data
files = dir('*.mat'); %list of .mat files
raw_data = [];
% loop through all .mat files and store as raw_data
for i = 1:length(files)
    eval(['load ' files(i).name]);
    raw_data = [raw_data; data];
end
save('rawdata.mat','raw_data')
csvwrite('rawdata.csv',raw_data)
clear data files i
%%
%%%
% create X and Y training data
X_train = raw_data(:,1:22);
Y_train = raw_data(:,24);

%%
%%%
% visualize data
x1 = X_train(:,1)./X_train(:,2);
x2 = X_train(:,3)./X_train(:,4);
x3 = X_train(:,8);
y = Y_train;

gscatter(x1,x3,y);
