from OpenCV_Functions import *

def drawRect(image, point1, point2, color=(255,0,0), thickness=1, linetype=cv2.LINE_AA ):
	result = imageCopy(image)
	return cv2.rectangle(result, point1, point2, color, thickness, linetype);


def imageProcessing(image): 
	result = imageCopy(image)
	resultcolor = convertColor(result, cv2.COLOR_BGRA2BGR)
	result = convertColor(result, cv2.COLOR_BGR2GRAY)
	height, width = result.shape[:2]

	threshold1=100
	threshold2=200
	result = cannyEdge(result, threshold1, threshold2)

	src_pt1 = (int(width)*0.45, int(height*0.65))
	src_pt2 = (int(width)*0.55, int(height*0.65))
	src_pt3 = (int(width), height)
	src_pt4 = (0, height)
	src_pts = np.float32( [src_pt1, src_pt2, src_pt3, src_pt4] )

	dst_pt1 = (int(width)*0.1, 0 )
	dst_pt2 = (int(width)*0.9, 0 )
	dst_pt3 = (int(width*0.9), height)
	dst_pt4 = (int(width*0.1), height)
	dst_pts = np.float32( [dst_pt1, dst_pt2, dst_pt3, dst_pt4] )

	result = imagePerspectiveTransformation(result, src_pts, dst_pts)

	lines = houghLinesP(result, 1, np.pi/180, 100)
	empty = np.zeros( (height, width), np.uint8)
	
	#print(empty.shape)
	#print(lines.shape)

	result = drawHoughLinesP(empty, lines)

	result = imagePerspectiveTransformation(result, dst_pts, src_pts)
	result = addImage(result, resultcolor)

	return result


def Video(openpath, savepath = "output.avi"):
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    #out = cv2.VideoWriter(savepath, fourcc, fps, (width, height), True)
    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
    cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)
    import OpenCV_Functions
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            output = imageProcessing(frame)
            # Write frame-by-frame
            #out.write(output)
            # Display the resulting frame
            cv2.imshow("Input", frame)
            cv2.imshow("Output", output)
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    #out.release()
    cv2.destroyAllWindows()
    return


road_video_01 = "./solidWhiteRight.mp4"

Video(road_video_01, "output.mp4")
