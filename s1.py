# importing cv2
import cv2
# path 
path = 'numpy.jpg'
# Reading an image in default mode
image = cv2.imread(path)
# Window name in which image is displayed
window_name = "Image'
# Start coordinate, here (2, 4)
# represents the top left corner of rectangle
start_point = (2, 4)
# Ending coordinate, here (300, 166)
# represents the bottom right corner of rectangle
end_point = (300, 166)
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Displaying the image 
cv2.imshow(window_name, image)
