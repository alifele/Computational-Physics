P_bar = mean(prob, 1);
P_bar = P_bar / P_bar(end);
%plot(x(1:end-1), P_bar)

mat = P_bar - P_bar.';
DX = x(1:end-1) - x(1:end-1)';

MAT = mat ./ (DX + 0.00001);
%MAT = mean(MAT,1);
%plot(x(1:end-1),MAT);
imagesc(MAT(1:1:end,1:1:end));
colorbar();

