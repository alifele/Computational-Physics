

[StarsX, CoresX] = Compute();
N_timeSteps = size(StarsX);
N_timeSteps = N_timeSteps(end);
t = 1;


for tt=1:N_timeSteps
    
    clf;
    axis square;
    box on;
    hold on;
    updatePlot(StarsX, CoresX,tt);
    t = t+1
    t = mod(t, N_timeSteps);
    java.lang.Thread.sleep(5);

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
