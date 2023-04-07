import cv2
import pytesseract
import win32com.client
from pytesseract import Output
from PIL import Image	
import pyttsx3
	


camera=cv2.VideoCapture(1)

while True:
	_,Image=camera.read()
	cv2.imshow('Text detection',Image)
	if cv2.waitKey(1)& 0xFF==ord('s'):
		cv2.imwrite('test1.jpg',Image)
		break
camera.release()
cv2.destroyAllWindows()
with open("OCR1.py") as f:
    exec(f.read())

