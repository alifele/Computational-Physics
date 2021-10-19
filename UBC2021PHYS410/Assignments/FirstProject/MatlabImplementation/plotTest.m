% M-file to place multiple small circles inside a big circle.
% Clean up
close all;
clc;
fontSize = 15;
% Initialize some parameters.
numberOfSmallCircles = 25; % Number of small circles
smallCircleOutsideValue = 0.2;
smallCircleInsideValue = 0.8;
smallCircleRadius = 25;    % small circle radius
bigImageWidth = 500;
bigImageHeight =  500; % square area 0f 500*500
bigCircleRadius = 250;    % big circle radius

% Initialize an image to hold one single big circle.
bigCircleImage = zeros(bigImageHeight, bigImageWidth);
[x, y] = meshgrid(1:bigImageWidth, 1:bigImageHeight);
bigCircleImage((x - bigImageWidth/2).^2 + (y - bigImageHeight/2).^2 <= bigCircleRadius.^2) = 1;
% Display it in the upper left plot.
subplot(3,2, 1);
imshow(bigCircleImage, []);
title('Big Circle Mask', 'FontSize', fontSize);
set(gcf, 'Position', get(0,'Screensize')); % Maximize figure.

% Initialize an image to hold one single small circle.
smallCircleImage = zeros(2*smallCircleRadius, 2*smallCircleRadius);
[x, y] = meshgrid(1:smallCircleRadius*2, 1:smallCircleRadius*2);
singleCircleImage = zeros(2*smallCircleRadius, 2*smallCircleRadius);
singleCircleImage((x - smallCircleRadius).^2 + (y - smallCircleRadius).^2 <= smallCircleRadius.^2) = smallCircleInsideValue;
% Display it in the upper right plot.
subplot(3,2, 2);
imshow(singleCircleImage, []);
title('Single Small Circle (scaled to fit)', 'FontSize', fontSize);

singleWidth = size(singleCircleImage, 2);
singleHeight = size(singleCircleImage, 1);
% Get random coordinates in the big image where
% we will place the upper left corner of the small circle.
widthThatWillFit = bigImageWidth - 2 * smallCircleRadius;
heightThatWillFit = bigImageHeight - 2 * smallCircleRadius;
smallUpperLeftX = widthThatWillFit * rand(numberOfSmallCircles, 1);
smallUpperLeftY = heightThatWillFit * rand(numberOfSmallCircles, 1);
% Initialize an output image to hold many small overlapping circles.
manySmallCircles = zeros(bigImageHeight, bigImageWidth);
% Place the small circles one by one.
for k = 1 : numberOfSmallCircles
	% Find the square in the big image where we're going to add a small circle.
	x1 = int16(smallUpperLeftX(k));
	y1 = int16(smallUpperLeftY(k));
	x2 = int16(x1 + singleWidth - 1);
	y2 = int16(y1 + singleHeight - 1);
	% Add in one small circle to the existing big image.
	manySmallCircles(y1:y2, x1:x2) = manySmallCircles(y1:y2, x1:x2) + singleCircleImage;
end
% Make outside the circles the outside color.
manySmallCircles(manySmallCircles == 0) = smallCircleOutsideValue;
% Display it in the lower left plot.
subplot(3,2, 3);
imshow(manySmallCircles);
title('Many Small Overlapping Circles', 'FontSize', fontSize);

% Multiply the big circle mask by the many small circles image to clip
% those small circles that lie outside the big circle.
maskedByBigCircle = bigCircleImage .* manySmallCircles;
% Display it in the lower right plot.
subplot(3,2, 4);
imshow(maskedByBigCircle);
title('Many Small Circles Masked by Big Circle', 'FontSize', fontSize);

% Take the histogram and display it in the bottom row.
subplot(3,2, 6);
hist(maskedByBigCircle(:));
grid on;
title('Histogram of Image Inside Big Circle', 'FontSize', fontSize);