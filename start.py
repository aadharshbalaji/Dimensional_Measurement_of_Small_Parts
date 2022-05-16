import glob
from Edge import Edge_Detection
class Start:
	def __init__(self):
		self.__file_count=0
		self.Detect_Edge()
	def Detect_Edge(self):	
		for __file in glob.glob("Dataset/train/good/*.png"):
			#Extract the file name from Dataset Folder
			self.__filename=__file[-7:]
			#Creating Object for Edge Detection Class
			self.__E=Edge_Detection(self.__filename)
		#	->Read the Image
		#	->Converting it into monochromatic Image
		#	->Detecting Edges.
			self.__E.read()
			self.__E.convert_gray()
			self.__E.edge_detection()
			self.__file_count+=1
	def __del__(self):
		print(self.__file_count)	
if __name__ == '__main__':
	start=Start()
	print("Executed Successfully!!!")
