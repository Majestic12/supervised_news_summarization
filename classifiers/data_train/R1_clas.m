% cls_db2.Prior = [1 1];
% R2 = confusionmat(cls_db2.Y,resubPredict(cls_db2));

R2 = cmat;
N  = sum(sum(R2));
R2_nom = R2/N;
TP = R2(1,1);
TN = R2(2,2);
FP = R2(1,2);
FN = R2(2,1);

Pd = TP/(TP+FN);
Pf = FP/(TN+FP);
pos_prec = TP/(TP+FP);
neg_prec = TN/(TN+FN);
CCR = (TP+TN)/N
mis_clas = (FP+FN)/N;
odds = (TP*TN)/(FP*FN);

Prow = sum(R2_nom');
Pcol = sum(R2_nom);
kappa = (CCR - sum(Prow.*Pcol))/(1 - sum(Prow.*Pcol))

Fscore = 2*Pd*pos_prec/(Pd+pos_prec)

% kappa = 2*Pcol(1)*Pcol(2)*(Pd-Pf)/(Pcol(2)+(Pcol(1)-Pcol(2))*(Pcol(2)*Pd + Pcol(1)*Pf))