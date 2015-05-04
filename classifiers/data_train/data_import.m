%%% load .txt file and save as .mat
% loops through s1 - s25 and d1 - d50 and creates .mat files
suffix = '_1';
suffix2 = '_2';
errorcode = [];
for ss=1:25
    clearvars -except errorcode ss dd suffix2 suffix
    
    for dd = 1:50
        story_id = strcat('s',num2str(ss));
        doc_id = strcat('d',num2str(dd));
        
        try
            fileid1_txt = strcat(story_id,doc_id,'.txt');
            A = importdata(fileid1_txt);
            data1 = A.data;

            fileid2_txt = strcat(story_id,doc_id,suffix,'.txt');
            B = importdata(fileid2_txt);
            data2 = B.data;

            fileid3_txt = strcat(story_id,doc_id,suffix2,'.txt');
            C = importdata(fileid3_txt);
            data3 = C.data;


            data = [data1(:,1:10) data2 data3 data1(:,11:12)];

            fileid_mat = strcat(story_id,doc_id,'.mat');
            save(fileid_mat,'data')
        catch
            errorcode = [errorcode;[ss dd]];
        end
    end
end

