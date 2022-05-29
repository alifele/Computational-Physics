function value = Exact_2d_sch(mx,my,X,Y,t)

    value = exp(-1i*(mx^2+my^2)*pi^2*t).*sin(mx*pi*X).*sin(my*pi*Y);

end