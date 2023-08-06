import cv2
import pytesseract
import win32com.client
from pytesseract import Output
from PIL import Image	
import pyttsx3
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shsha\AppData\Local\Tesseract-OCR\tesseract.exe'
img1 = Image.open('test1.jpg')

# describes image format in the output
print(img1)						
# path where the tesseract module is installed
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img1)
# write text in a text file and save it to source path
with open('abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(result)
