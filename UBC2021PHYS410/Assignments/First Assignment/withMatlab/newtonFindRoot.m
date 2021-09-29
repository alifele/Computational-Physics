function root = newtonFindRoot(F,x_root, max_iteratin, DeltaX_limit, dx)
    
    DeltaX = 2*DeltaX_limit;
    iteration = 0;

    while (abs(DeltaX) > DeltaX_limit & iteration<max_iteratin & DeltaX~=0)
        DeltaX = F(x_root)/DF(@F, x_root, dx);
        x_root = x_root - DeltaX;
        iteration = iteration +1;

    end
    

    root = x_root;

end

% def findRoot(x_root, max_iteration, DeltaX_limit, dx):
%     DeltaX = 2*DeltaX_limit
%     iteration = 0
%     while (np.abs(DeltaX) > DeltaX_limit and iteration < max_iteration and DeltaX!=0):
%         DeltaX = F(x_root)/DF(x_root,dx)
%         x_root = x_root - DeltaX
%         iteration += 1
%     return x_root