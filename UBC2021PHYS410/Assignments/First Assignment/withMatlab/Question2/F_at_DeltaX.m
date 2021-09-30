function result = F_at_DeltaX(X, fNumber, varNumber, dh)
    
    %var number is the variable that varies (e.g. 1 is x)
    %fNumber is the function we are interested in (e.g. 1 is f_1)

    Xnew = X;
    Xnew(varNumber) = Xnew(varNumber) + dh;
    
    f = F(Xnew);
    result = f(fNumber);


end


% def FatDelta(X, fNumber, varNumber, dh): # varNumber is the varible that varies. if var = 1 then this function returns rondF/rondx
%     Xnew = np.copy(X)
%     Xnew[varNumber] += dh
%     return F(Xnew)[fNumber][0]
