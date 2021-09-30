function result = giveIntervalswithRoot(F, xmin, xmax)
    
    intervals = randomIntervals([xmin,xmax],15);
    intervalMult = F(intervals) .* circshift(F(intervals),-1);
    intervalwithRoots = [];
     
    i=1;
    for i = [1:length(intervalMult)-1]
        if (intervalMult(i)<0)
            intervalwithRoots(end+1,:) = [intervals(i), intervals(i+1 )];
        end
    end
    
    result = intervalwithRoots;
    
end






% 
% def giveIntervalswithRoot():
%     intervals = RandomInterval([-1,1],15)
%     intervalMult = F(intervals) * np.roll(F(intervals), -1)
%     intervalwithRoot = []
%     for i, elem in enumerate(intervalMult[:-1]):
%         if elem<0:
%             intervalwithRoot.append([intervals[i],intervals[i+1]])
% 
%     intervalwithRoot = np.array(intervalwithRoot)
%     return intervalwithRoot
% 
%     