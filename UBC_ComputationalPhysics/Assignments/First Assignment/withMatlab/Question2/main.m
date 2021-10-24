dh = 1E-5;
tol = 1E-8;
max_iteration = 50;
X = [3,-2,-1];


root = newtond(@F,@Jacobian,dh,X,tol,max_iteration);

root