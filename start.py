import glob
from Edge import Edge_Detection
from Dimensions import Dimension

class Start:
	def __init__(self):
		self.__file_count=0
		self.Detect_Edge()
		self.Dimensions_Measurement()
	def Detect_Edge(self):	
		for __file in glob.glob("Dataset/train/good/*.png"):
		#Extract the file name from Dataset Folder
			self.__filename=__file[-7:]
		#Creating Object for Edge Detection Class
			self.__E=Edge_Detection(self.__filename)
		#Read the Image
			self.__E.read()
			
		#Converting it into monochromatic Image
			self.__E.convert_gray()
			
		#Detecting Edges.
			self.__E.edge_detection()
			
			self.__file_count+=1
	def Dimensions_Measurement(self):
		for __file in glob.glob("Edge_Detected_Images/Train/good/*.png"):		
			
			self.__filename=__file[-7:]
			self.__D=Dimension(self.__filename)
			img=self.__D.align_text()
			self.__D.principal_axis()
				
	def __del__(self):
		print(self.__file_count)	
if __name__ == '__main__':
	start=Start()
	print("Executed Successfully!!!")
