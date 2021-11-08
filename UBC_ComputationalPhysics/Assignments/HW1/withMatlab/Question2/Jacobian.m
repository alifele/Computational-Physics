function result = Jacobian(F, X, dh)

    n = 3;
    result = zeros(n);

    for i=[1:n]
        for j=[1:n]
            fval = F(X);
            result(i,j) = (F_at_DeltaX(X,i,j,dh) - fval(i))/dh;
        end
    end

end




% 
% def J(X):
%     n = 3
%     result = np.zeros((n,n), dtype='float64')
%     
%     for i in range(n):
%         for j in range(n):
%             result[i,j] = (FatDelta(X,i,j,dh) - F(X)[i][0])/dh
%             
%     return result