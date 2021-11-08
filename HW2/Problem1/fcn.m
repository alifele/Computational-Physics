function out = fcn(x, Y)
    mu = 2;
    F1 = Y(2);
    F2 = mu*(1-Y(1)^2)*Y(2) - Y(1);

    out = [F1; F2];

end