dx = 1E-5;
deltaX_limit = 1E-13;
max_iteration = 100;

xmin = -1;
xmax = 1;

tol1 = 1E-5;
tol2 = 1E-12;

n_Ensemble = 1;


allRoots = [];

for i=[1:n_Ensemble]
    roots = hybrid(@F, @DF, xmin, xmax, tol1, tol2,dx);
    for root=roots
        if not (any(allRoots == round(root,12)))
            allRoots(end+1) = root;
        end
    end

end



allRoots

