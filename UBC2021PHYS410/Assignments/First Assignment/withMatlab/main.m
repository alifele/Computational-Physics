dx = 1E-5;
deltaX_limit = 1E-12;
max_iteration = 100;

x_root = 0.1;


intervals = giveIntervalwithRoot(@F);
root_seeds = mean(intervals, 2)';

rootList= [];
for i=root_seeds
    root = newtonFindRoot(@F,i, max_iteration, deltaX_limit, dx);
    rootList(end+1) = root;
    
end


rootList