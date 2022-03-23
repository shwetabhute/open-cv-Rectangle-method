import cv2
path = 'numpy.jpg'
image = cv2.imread(path)
window_name = 'Image'
start_point = (2, 4)
end_point = (300, 166)
color = (255, 0, 0)
thickness = 2
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow(window_name, image)
