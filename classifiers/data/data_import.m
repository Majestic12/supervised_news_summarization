%%% load .txt file and save as .mat
clear all
story_id = 's3';
doc_id = 'd21';
suffix = '_1';
fileid1_txt = strcat(story_id,doc_id,'.txt');
A = importdata(fileid1_txt);
data1 = A.data;
fileid2_txt = strcat(story_id,doc_id,suffix,'.txt');
B = importdata(fileid2_txt);
data2 = B.data;

data = [data1(:,1:10) data2 data1(:,11:12)]

fileid_mat = strcat(story_id,doc_id,'.mat');
save(fileid_mat,'data')
