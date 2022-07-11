function result = integral_array(data, tList)

dtList = circshift(tList,-1) - tList;
dtList = dtList(1:end-1);

summedData = circshift(data,-1) + data;
summedData = summedData(1:end-1,:);

result = summedData' * dtList;

end


% ###### Function debug testbench #######
% Based on the following debug test, this function works properly

% tList = rand(100,1)*10;
% tList = sort(tList);
% data = tList.^2;
% dtList = circshift(tList,-1) - tList;
% dtList = dtList(1:end-1);
% 
% summedData = (circshift(data,-1) + data)/2;
% summedData = summedData(1:end-1,:);
% result = summedData' * dtList
% 
% % plot(tList, data,"o")
% % hold on;
% % plot(tList(1:end-1), summedData)

