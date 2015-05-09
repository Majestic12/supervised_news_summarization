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

