function result = DF(F,x,dx)

    result = (-3*F_at_xplusdx(@F,x,dx,0) + 4*F_at_xplusdx(@F,x,dx,1) - F_at_xplusdx(@F,x,dx,2))/(2*dx);

end
