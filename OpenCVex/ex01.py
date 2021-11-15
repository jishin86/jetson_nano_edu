from OpenCV_Functions import *

def imageProcessing(image): 
	result = imageCopy(image)
	for i in range(0,200):
		for j in range(0,200):
			result = setPixel(result, i, j, [0,0,0])
	return result


road_image_01 = "./solidWhiteCurve.jpg"

image = imageRead(road_image_01, cv2.IMREAD_COLOR)

result = imageProcessing(image)

imageShow("image_color, cv2.WINDOW_NORMAL", result, cv2.WINDOW_NORMAL)


