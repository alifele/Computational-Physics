function [x, y, t, psi, psire, psiim, psimod, v] = ...
    sch_2d_adi(tmax, level, lambda, idtype,  idpar, vtype, vpar)

    %% Discrete Initiate
        dx = 2^(-level);
        dy = dx;
        dt = lambda * dx;
        xList = [0:dx:1];
        yList = [0:dy:1];
        tList = [0:dt:tmax];
        nx = size(xList, 2);
        nt = size(tList, 2);
        [X,Y] = meshgrid(xList, yList);
    
        psi_t = zeros(nx,nx) * 1i;
        psiData = zeros(nx,nx,nt) * 1i;
        R = dt/(dx^2);
    
    
    %% Evaluate idtype
        if idtype == 0
           mx = idpar(1);
           my = idpar(2);
           psi_t = sin(mx*pi*X) .* sin(my*pi*Y);
        end
        
        if idtype == 1
           x0 = idpar(1);
           y0 = idpar(2);
           deltax = idpar(3);
           deltay = idpar(4);
           px = idpar(5);
           py = idpar(6);
           psi_t = exp(1i*px*X) .* exp(1i*py*Y) .* exp(-(((X-x0)/deltax).^2 + ((Y-y0)/deltay).^2));
        
        end
    
    
    %% Evaluate vtype
        V = zeros(nx,nx);
        if vtype == 1
           x_min = vpar(1);
           x_max = vpar(2);
           y_min = vpar(3);
           y_max = vpar(4);
           Vc = vpar(5);
           V((X>x_min)&(X<x_max)&(Y>y_min)&(Y<y_max)) = Vc;
        end

        if vtype ==2
            x1 = vpar(1);
            x2 = vpar(2);
            x3 = vpar(3);
            x4 = vpar(4);
            Vc = vpar(5);

            [x1,i1] = min(xList<x1);
            [x2,i2] = min(xList<x2);
            [x3,i3] = min(xList<x3);
            [x4,i4] = min(xList<x4);

            jp = (nx-1)/4+1;
            V(:,jp) = Vc;
            V(:,jp+1) = Vc;
            V(i1:i2,jp) = 0;
            V(i3:i4,jp) = 0;
            V(i1:i2,jp+1) = 0;
            V(i3:i4,jp+1) = 0;
            

        end
    
    %% Solve

    
    %%% Create Delta and Tilda
        upDiag = ones(nx,1);
        Diag = ones(nx,1)*(-2);
        lowDiag = ones(nx,1);
        upDiag(2) = 0;
        lowDiag(nx-1) = 0;
        Diag(1) = 1;
        Diag(end) = 1;
        Delta = spdiags([lowDiag, Diag, upDiag],-1:1,nx,nx);
        
        DtildaY = Delta - dt/R * V;
        DtildaX = Delta - dt/R * V.';
     
    
    %%% Create abcd
        Mx = eye(nx) - 1i*R/2 * DtildaX;
        My = eye(nx) + 1i*R/2 * DtildaY;
        M_p = eye(nx) + 1i*R/2 * Delta;
        M_m = eye(nx) - 1i*R/2 * Delta;

        ab = M_m\My;            %inv(M_m) * My
        cd = (Mx\M_p).';        %(inv(Mx)*M_p).'

    %%% Loop to Solve
        for tt = 1:nt
          psiData(:,:,tt) = psi_t;
          psi_t = ab * psi_t * cd;

        end


    %% Set Returns
        x = xList;
        y = yList;
        t = tList;
        psi = psiData;
        psire = real(psiData);
        psiim = imag(psiData);
        psimod = abs(psiData);
        v = V; 
      

end