function updatePlot(StarsX, CoresX, t)

    shapeStarsX = size(StarsX);
    NStars = shapeStarsX(1);


    shapeCoresX = size(CoresX);
    NCores = shapeCoresX(1);

    NtimeSteps = shapeStarsX(end);
    
    

    
    scatter(StarsX(:,1,t),StarsX(:,2,t),5, "Marker","o", "MarkerFaceColor","red", "MarkerEdgeColor","red")
    scatter(CoresX(:,1,t),CoresX(:,2,t),30, "Marker","o", "MarkerFaceColor","yellow", "MarkerEdgeColor","black")
    xlim([-10,10]);
    ylim([-10,10]);
    drawnow;
   

  


end