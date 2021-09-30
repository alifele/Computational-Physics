function result = F(X)
    x = X(1);
    y = X(2);
    z = X(3);

    f1 = x.^2 + y.^3 + z.^4 - 1;
    f2 = sin(x.*y.*z) - x - y - z;
    f3 = x - y.*z;

    result = [f1;f2;f3];
    

end




% def F(X):
%     x = X[0][0]
%     y = X[1][0]
%     z = X[2][0]
%     f1 = x**2 + y**3 + z**4 -1
%     f2 = np.sin(x*y*z)-x-y-z
%     f3 = x - y*z
% 
% #     #For Test
% #     f1 = 2*x + y + z/2
% #     f2 = 2*y + x/2 + z
% #     f3 = 2*z - x - y
%     
%     return np.array([f1,f2,f3]).reshape((3,1))