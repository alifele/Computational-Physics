dx = 1E-5;
deltaX_limit = 1E-12;
max_iteration = 100;

x_root = 0.1;

root = newtonFindRoot(@F,x_root, max_iteration, deltaX_limit, dx);
root
