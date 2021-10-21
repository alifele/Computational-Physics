

l = 10;
tmax = 12; %25


[StarsX, CoresX] = Compute(l, tmax);
N_timeSteps = size(StarsX);
N_timeSteps = N_timeSteps(end);
t = 1;

generateOutPut = 1;



if generateOutPut ~= 1
%     Core1X = reshape(CoresX(1,1,:),1,[]);
%     Core1Y = reshape(CoresX(1,2,:),1,[]);
%     plot(Core1X)
ConvergenceTest(tmax);
end




if generateOutPut == 1

%     avifilename = 'GalaxyCollisionCenterofMass.avi';
%     aviobj = VideoWriter(avifilename);
%     open(aviobj);
    
    
    
    
    for j=1:1
    
        for tt=1:N_timeSteps
            
            clf;
            axis square;
            box on;
            hold on;
            updatePlot(StarsX, CoresX,tt);
%             updatePlot(StarsX, CoresX,tt, aviobj);
            t = t+1
            t = mod(t, N_timeSteps);
            %java.lang.Thread.sleep(100);
        
        end 
    
    end
    
%      close(aviobj);

end



% from sys import exit
% from sketch import *
% from Compute import *
% 
% pygame.init()
% sketch = Sketch()
% sketch.setup()
% 
% StarsX, CoresX = Compute()
% t = 0
% 
% while True:
%     for event in pygame.event.get():
%         if event.type == QUIT:
%             pygame.quit()
%             exit()
% 
%     sketch.update(StarsX, CoresX, t)
%     t+=1
%     t = t % StarsX.shape[-1]
%     pygame.time.delay(5)
%     print(t)
