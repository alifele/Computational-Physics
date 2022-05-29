function value = exact_1d_sch(m,x,t)

    value = exp(-1i*m^2*pi^2*t).*sin(pi*m*x);

end