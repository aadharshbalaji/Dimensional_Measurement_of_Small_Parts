import cv2
import numpy as np
import imutils
from imutils import perspective
from imutils import contours
from scipy.spatial.distance import euclidean

class Edge_Detection:
	def __init__(self,name):
		self.__Source_path = "Dataset/train/good/"+name
		self.__Destination_path = "Edge_Detected_Images/Train/good/"+name
		
	#To show image
	def show(self,images):
	    for k, img in enumerate(self.images):
	    	cv2.imshow("image_" + str(k), img)
	    cv2.waitKey(0)
	    cv2.destroyAllWindows()

	def read(self):
		# Reading Image
		self.__image = cv2.imread(self.__Source_path)
	
	def convert_gray(self):
	# Setting gray and blur
		try:
			self.__gray = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
			self.__blur = cv2.GaussianBlur(self.__gray, (9, 9), 0)
		except Exception as E:
			pass
		
	def edge_detection(self):
		try:
			self.__edge = cv2.Canny(self.__blur, 50, 100)
			self.__edge = cv2.dilate(self.__edge, None, iterations=1)
			self.__edge = cv2.erode(self.__edge, None, iterations=1)

			# Contours
			cn = cv2.findContours(self.__edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			cn = imutils.grab_contours(cn)

			cv2.imwrite(""+self.__Destination_path,self.__edge)
		except Exception as E:
			pass
