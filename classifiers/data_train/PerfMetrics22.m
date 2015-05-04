function [ CCR, Fscore, Kappa] = PerfMetrics22( C22 )
%Performance Metrics based on 2 by 2 confusion matrix
%   C22 : 2 by 2 confusion matrix in MATLAB
M = C22';
TP = M(1,1);FP = M(1,2);
FN = M(2,1);TN = M(2,2);
N = TP + FP + FN + TN;
CCR = (TP+TN)/N;

Prow = [TP+FP;FN+TN]/N;
Pcol = [TP+FN;FP+TN]/N;
Kappa = (CCR - Prow'*Pcol)/(1-Prow'*Pcol);

P = TP/(TP+FP);
R = TP/(TP+FN);
Fscore = 2*P*R/(P+R);

end

