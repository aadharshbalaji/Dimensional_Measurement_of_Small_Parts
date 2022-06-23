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
		self.__Gray_path="GrayScaled/Train/GrayScaled"+name
		self.__Gaussian_path="Gaussian/Train/Gaussian"+name
		self.__Canny_path="Canny/Train/Canny"+name
		self.__Dilated_path="Dilated/Train/Dilated"+name
		self.__Eroded_path="Eroded/Train/Eroded"+name
		
	
	#To show image
	def show(self,images):
	    for k, img in enumerate(images):
	    	cv2.imshow("image_" + str(k), img)
	    cv2.waitKey(0)
	    cv2.destroyAllWindows()

	# Reading Image
	def read(self):
		self.__image = cv2.imread(self.__Source_path)
	
	# Setting gray and blur
	def convert_gray(self):
		try:
			self.__gray = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
			cv2.imwrite(""+self.__Gray_path,self.__gray)
			self.__blur = cv2.GaussianBlur(self.__gray, (9, 9), 0)
			cv2.imwrite(""+self.__Gaussian_path,self.__blur)
		except Exception as E:
			print(E)
		
	def edge_detection(self):
		try:
			self.__edge = cv2.Canny(self.__blur, 50, 100)
			cv2.imwrite(""+self.__Canny_path,self.__edge)
			self.__edge = cv2.dilate(self.__edge, None, iterations=1)
			cv2.imwrite(""+self.__Dilated_path,self.__edge)
			self.__edge = cv2.erode(self.__edge, None, iterations=1)
			cv2.imwrite(""+self.__Eroded_path,self.__edge)

	# Contours
			cn = cv2.findContours(self.__edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			self.cnts = imutils.grab_contours(cn)
			
			cv2.imwrite(""+self.__Destination_path,self.__edge)
		except Exception as E:
			print(E)
			
	def convert_to_numpy(self):
		try:
			self.__npimage=np.array(self.__edge)
			self.n=1
			while self.n==1:
				print(__npimage)
		
		except Exception as E:
			print(E)
