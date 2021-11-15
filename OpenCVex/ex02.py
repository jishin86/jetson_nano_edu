from OpenCV_Functions import *

def imageProcessing(image): 
	result = imageCopy(image)
	result = convertColor(result, cv2.COLOR_BGR2HLS)
	h,l,s = splitImage(result)
	for i in range(0,200):
		for j in range(0,200):
			l2 = setPixel(l, i, j, 200)
	result = mergeImage(h, l2, s)
	result = convertColor(result, cv2.COLOR_HLS2BGR)
	return result


road_image_01 = "./solidWhiteCurve.jpg"

image = imageRead(road_image_01, cv2.IMREAD_COLOR)

result = imageProcessing(image)

imageShow("image_color, cv2.WINDOW_NORMAL", result, cv2.WINDOW_NORMAL)


