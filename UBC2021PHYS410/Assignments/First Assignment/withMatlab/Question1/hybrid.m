function x = hybrid(f,dfdx,xmin,xmax,tol1, tol2, dx)


    

    intrervalswithRoot = giveIntervalwithRoot(f, xmin, xmax);
    rootSeeds = [];

    for i = [1:length(intrervalswithRoot)]
        rootSeeds(end+1) = Bisection(f, intrervalswithRoot(i,:), 10);

    end

    roots = [];

    for i = [1:length(rootSeeds)]
        roots(end+1) = newtonFindRoot(f,rootSeeds(i),20,tol2, dx);
    
    end

    x = roots;


end


% 
% def runHybrid():
%     intervalswithRoot = giveIntervalswithRoot()
%     rootSeeds = []
%     for elem in intervalswithRoot:
%         rootSeeds.append(iterateBisection(elem, 10, Function=F))
%         
%     roots = []
%     for elem in rootSeeds:
%         roots.append(findRoot(elem, max_iteration, DeltaX_limit, dx))
% 
%     return roots