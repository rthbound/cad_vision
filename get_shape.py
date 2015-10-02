import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def resize_img(img):
	#print img.shape
	# we need to keep in mind aspect ratio so the image does
	# not look skewed or distorted -- therefore, we calculate
	# the ratio of the new image to the old image
	#r = 100.0 / img.shape[1]
	#dim = (100, int(img.shape[0] * r))
	#dim = (640,480)
	#print dim
	# perform the actual resizing of the image and show it
	#resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	#print resized.shape
	#cv2.imshow("resized", resized)
	return resized

if __name__=="__main__":

	img = None

	try:
		img = cv2.imread('images/EOS_650D_Top_View.jpg')
	
	except:
		pass
	
	if len(sys.argv) > 1:
		try:
			img = sys.argv[1]
		except:
			print "******* Could not open image file *******"
			print "Unexpected error:", sys.exc_info()[0]
			#raise		
			sys.exit(-1)

	import numpy as np

	def nothing(x):
		pass
		
	#img = resize_img(img)
	dim = (640,480)
	resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	#image window
	cv2.namedWindow('image')

	# create trackbars for color change
	cv2.createTrackbar('th1','image',0,255,nothing)
	cv2.createTrackbar('th2','image',0,255,nothing)

	while(1):
		# get current positions of four trackbars
		th1 = cv2.getTrackbarPos('th1','image')
		th2 = cv2.getTrackbarPos('th2','image')
		#apply canny 
		edges = cv2.Canny(resized_img,th1,th2)
		#show the image
		cv2.imshow('image',edges)
		#press ESC to stop
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
		    break

	cv2.destroyAllWindows()
	
