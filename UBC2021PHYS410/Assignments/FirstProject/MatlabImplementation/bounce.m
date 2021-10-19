% bounce: Bouncing ball animation with optional AVI 
% creation
%
% Presented here principally as an illustration of the 
% creation of AVI movies.  Search for 'avi' to locate 
% pertinent blocks of code.
%-----------------------------------------------------------
% Parameters defining discrete set of times.
%-----------------------------------------------------------
tmax = 3;
deltat = 0.01;   

%-----------------------------------------------------------
% Coefficient of restitution. Reflected velocity component 
% is a factor of kappa times the incident component.  
% due to a bounce by setting kappa smaller, or a gain
% ("activating floor) by setting kappa > 1.
%-----------------------------------------------------------
kappa = 0.98;

%-----------------------------------------------------------
% Acceleration of ball. a is a two-element vector with
% constant x- and y-components. I've tuned g and the initial
% y-velocity to produce a reasonable looking simulation.
%-----------------------------------------------------------
g = -20;
a = [0.0, g];

%-----------------------------------------------------------
% Initial position and velocity of ball. r and v are two
% component vectors.
%-----------------------------------------------------------
x0 = 0.0;
y0 = 1.0;
r = [x0, y0];

vx0 = 0.5;
vy0 = 0.0;
v = [vx0, vy0];

%-----------------------------------------------------------
% Bounce counter.
%-----------------------------------------------------------
nbounce = 0;

%-----------------------------------------------------------
% Set plotenable to non-zero/zero to enable/disable plotting.
%-----------------------------------------------------------
plotenable = 1;
%-----------------------------------------------------------
% Parameter to control speed of animation.  Script execution
% will pause for pausesecs each time a new frame is drawn.
% 
% Setting this parameter to a "largish" value, say 0.1
% (seconds), will produce a slow-motion effect.
% 
% Set it to 0 for maximum animation speed.
%-----------------------------------------------------------
pausesecs = 0.01;

%-----------------------------------------------------------
% Plot attributes defining the appearance  of the ball.
%-----------------------------------------------------------

% Ball has a (marker) size of 15 ...
ballsize = 15;
% ... it's red ...
ballcolor = 'r';
% ... and it's plotted as a circle.
ballmarker = 'o';

%-----------------------------------------------------------
% Define the coordinates for the floor and the properties for 
% the plot command that define the appearance of the floor.  
%-----------------------------------------------------------

% Parameters that define the floor position and length.
fxmin = 0.0;
fxmax = 1.0;
fy = 0.0;

% 2 x 2 matrix of floor coordinates those parameters.
fxy = [[fxmin, fxmax]; [fy, fy]];

%-----------------------------------------------------------
% Plot attributes defining the appearance of the floor.
%-----------------------------------------------------------

% The floor is blue ...
fcolor = 'b';
% ... and we'll draw it using a fairly thick line.
fwidth = 5;

%-----------------------------------------------------------
dlim = 0.15;

%-----------------------------------------------------------
% Set avienable to a non-zero value to make an AVI movie.
%-----------------------------------------------------------
avienable = 1;

% If plotting is disabled, ensure that AVI generation
% is as well
if ~plotenable
   avienable = 0;
end

% Name of avi file.
avifilename = 'bounce.avi';

% Presumed AVI playback rate in frames per second.
aviframerate = 25;



%-----------------------------------------------------------
%% SECTION 2. PERFORM THE SIMULATION.
%-----------------------------------------------------------

%-----------------------------------------------------------
% If AVI creation is enabled, then initialize an avi object.
%-----------------------------------------------------------
if avienable
   aviobj = VideoWriter(avifilename);
   open(aviobj);
end

%-----------------------------------------------------------
% FOR EACH TIME STEP ...
%-----------------------------------------------------------

for t = 0 : deltat : tmax
   % BEGIN TIME STEP
    
   if plotenable
      %%-----------------------
      %% BEGIN Graphics section
      %%-----------------------

      % Clear figure
      clf;

      % Don't erase figure after each plot command.
      hold on;

      % Define plotting area, using a 1:1 aspect ratio for the 
      % plotted region, boxed axes and a 15%-width "border" around 
      % the unit square.
      axis square;
      box on;
      xlim([-dlim, 1 + dlim]);
      ylim([-dlim, 1 + dlim]);

      % Make and display title. 
      titlestr = sprintf('Step: %d   Time: %.1f  Number of bounces: %d', ...
         fix(t / deltat), t, nbounce);
      title(titlestr, 'FontSize', 16, 'FontWeight', 'bold', ...
         'Color', [0.25, 0.42, 0.31]);

      % Draw the floor.
      plot(fxy(1,:), fxy(2,:), 'Color', fcolor, 'LineWidth', fwidth);

      % Draw the ball. 
      plot(r(1), r(2), 'Marker', ballmarker, 'MarkerSize', ballsize, ...
         'MarkerEdgeColor', ballcolor, 'MarkerFaceColor', ballcolor);

      % Force update of figure window.
      drawnow;

      % Record video frame if AVI recording is enabled and record 
      % multiple copies of the first frame.  Here we record 5 seconds
      % worth which will allow the viewer a bit of time to process 
      % the initial scene before the animation starts.
      if avienable
         if t == 0
            framecount = 5 * aviframerate ;
         else
            framecount = 1;
         end
         for iframe = 1 : framecount
            writeVideo(aviobj, getframe(gcf));
         end
      end

      % Pause execution to control interactive visualization speed.
      pause(pausesecs);
      %%-----------------------
      %% End Graphics section
      %%-----------------------
   end

   %%--------------------------
   %% Particle dynamics section
   %%--------------------------

   % Update the velocity.
   v = v + deltat * a;

   % Compute provisional change in ball's position.
   dr = deltat * v;

   % Check for an intersection with the floor. 
   if ( r(2) + dr(2) < fxy(2,1) )  &  ( fxy(1,1) <= r(1) & r(1) <= fxy(1,2) )
      % Provisional particle position IS below the floor.

      % Reverse sign of v_y, and scale it by the coefficient of 
      % restitution.
      v(2) = - kappa * v(2);

      % Don't change the particle's y coordinate.
      dr(2) = 0;
      % Update the bounce count.
      nbounce = nbounce + 1;

   end 

   % Update the position.
   r = r + dr;

   % END TIME STEP
end

% END SIMULATION

% If we're making a video, finalize the recording and 
% write a diagnostic message that a movie file was created.

if avienable
   close(aviobj);
   fprintf('Created video file: %s\n', avifilename);
end
% END OF SCRIPT
