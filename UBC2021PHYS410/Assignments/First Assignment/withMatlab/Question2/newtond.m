function result = newtond(f,jacfd,h,x0,tol, max_iteration)
    X = x0;
    deltaX = 2*tol;
    iteration = 1;
    while(norm(deltaX)>tol & norm(deltaX)~=0 & iteration<max_iteration)

        deltaX = inv(jacfd(f,X,h))*f(X);
        X = X - deltaX';
        iteration = iteration+1;

    end


    result = X;

end





% def runNewton(X, dh, Error, max_iteration):
%     deltaX = 2*Error
%     iteration = 0
%     while(np.linalg.norm(deltaX)>Error and np.linalg.norm(deltaX)!=0 and iteration<max_iteration):
%         deltaX = np.matmul(np.linalg.inv(J(X)), F(X))
%         X -= deltaX
%         iteration+=1
%     
%     print(iteration)
%     return X