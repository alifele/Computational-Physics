function updatePlot(StarsX, CoresX, t)

    shapeStarsX = size(StarsX);
    NStars = shapeStarsX(1);


    shapeCoresX = size(CoresX);
    NCores = shapeCoresX(1);

    NtimeSteps = shapeStarsX(end);
    
    s = scatter(StarsX(NStars/2+1:end,1,t),StarsX(NStars/2+1:end,2,t),15,'filled', "Marker","o", "MarkerFaceColor","green");
    s.MarkerFaceAlpha = 0.6;
    s = scatter(StarsX(1:NStars/2,1,t),StarsX(1:NStars/2,2,t),15,'filled',"Marker","o", "MarkerFaceColor","red");
    s.MarkerFaceAlpha = 0.2;
    s = scatter(CoresX(:,1,t),CoresX(:,2,t),180,'filled', "Marker","o", "MarkerFaceColor","yellow", "MarkerEdgeColor","black");
    s.MarkerFaceAlpha = 1;



%     s = scatter(StarsX(1:NStars/2,1,t),StarsX(1:NStars/2,2,t),5, "Marker","o", "MarkerFaceColor","red", "MarkerEdgeColor","red");
%     s.MarkerFaceAlpha = 0.5;
%     s = scatter(StarsX(NStars/2+1:end,1,t),StarsX(NStars/2+1:end,2,t),5, "Marker","o", "MarkerFaceColor","green", "MarkerEdgeColor","green");
%     s.MarkerFaceAlpha = 0.5;
%     s = scatter(CoresX(:,1,t),CoresX(:,2,t),180, "Marker","o", "MarkerFaceColor","yellow", "MarkerEdgeColor","black");
%     s.MarkerFaceAlpha = 1;
%     
%     
%     

        

    xlim([-10,10]);
    ylim([-10,10]);
    drawnow;
   

  


end