%%% load .txt file and save as .mat
% loops through s1 - s25 and d1 - d50 and creates .mat files
suffix = '_1';
suffix2 = '_2';

ss = 19;

for dd = 1:50
    story_id = strcat('s',num2str(ss));
    doc_id = strcat('d',num2str(dd));
    try
        data = [data; importdata(strcat(story_id,doc_id,'.mat'))];
    catch
    end
end
clearvars -except data
%%
fileid_mat = strcat('data_test_econ.mat');
save(fileid_mat,'data')

%%
