function result = Bisection(F, interval, max_iteration)

    a = interval(1);
    b = interval(2);
    
    for i=[1:max_iteration]
        
        if (F((a+b)/2).*F(b) > 0)
            b = (a+b)/2;
        else
            a = (a+b)/2;
        end
    
    end

    result = (a+b)/2

end


% def iterateBisection(interval, iteration, Function):
%     a = interval[0]
%     b = interval[1]
%     for i in range(iteration):
%         if (Function((a+b)/2)*Function(b) > 0):
%             b = (a+b)/2
%         else:
%             a = (a+b)/2
%             
%     return (a+b)/2