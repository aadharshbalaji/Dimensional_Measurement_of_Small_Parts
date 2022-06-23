import numpy as np
import cv2
from PIL import Image
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import pdist

class Dimension:
	def __init__(self,name):
		self.__Source_path = "Dataset/train/good/"+name
		self.__Destination_path = "Edge_Detected_Images/Train/good/"+name
		self.__Rotated_path = "Rotated/train/good/"+name
		self.__Gray_path="GrayScaled/Train/"+name
		self.__Gausssian_path="Gaussian/Train/"+name
		self.__Canny_path="Canny/Train/"+name
		self.__Dilated_path="Dilated/Train/Dilated"+name
		self.__Eroded_path="Eroded/Train/Eroded"+name
		self.__filename=name
	
	#To show image
	def show(self,images):
	    for k, img in enumerate(images):
	    	cv2.imshow("image_" + str(k), img)
	    cv2.waitKey(0)
	    cv2.destroyAllWindows()

	
	def align_text(self):
		
		img=np.array(Image.open(self.__Destination_path))
		
	# apply image thresholding
		img_thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	# invert the image, 255 is the maximum value
		img_thresh = 255 - img_thresh
	# display image
		coords = np.column_stack(np.where(img_thresh > 0))
		angle = cv2.minAreaRect(coords)[-1]
		if angle < 90:
			angle = -(90 + angle)
		else:
			angle = -angle
		h,w = img.shape
		center = (w // 2, h // 2)
		M = cv2.getRotationMatrix2D(center, angle, 1.0)
		self.rotated = cv2.warpAffine(img_thresh, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
		cv2.imwrite(self.__Rotated_path,self.rotated)
		return self.rotated
		
		
	# Reading Image
	def read(self):
		print(self.__Destination_path)
		self.__image = cv2.imread(self.__Eroded_path)
		
	def principal_axis(self):
		self.__image = self.rotated
		ref=125
		P1P2_mm=max(pdist(self.__image))/ref
		file1 = open("MyFile.txt", "a")
		file1.write("\n"+self.__filename+" "+ str(P1P2_mm))
		file1.close() 
	
	# Setting gray and blur
	def convert_to_numpy(self):
		try:
			self.__npimage=np.array(self.__image)
			print(__npimage)
		
		except Exception as E:
			print(E)
		
	
