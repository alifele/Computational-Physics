function result = randomIntervals(interval, n_intreval)

    stepSize = (interval(2)-interval(1))/n_intreval;
    intervalPoints=[interval(1)];

    while(intervalPoints(end)<interval(2))
        nextVal = (intervalPoints(end)+rand()*stepSize);
        intervalPoints(end+1) = nextVal;
    end
    intervalPoints(end) = interval(2);
    result = intervalPoints;


end



% 
% def RandomInterval(interval, n_interval): #interval = [-1,1]
%     stepSize = (interval[1]-interval[0])/n_interval # 2 is the [-1,1] interval length
% 
%     intervalPoints = [interval[0]]
%     while (intervalPoints[-1]<1):
%         nextVal = (intervalPoints[-1] +np.random.random()*stepSize)
%         intervalPoints.append(nextVal)
% 
%     intervalPoints[-1] = interval[1]
%     intervalPoints = np.array(intervalPoints)
%     
%     return intervalPoints