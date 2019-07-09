
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract '
#text = pytesseract.image_to_string(Image.open('OCR.png'),lang = 'eng')
#print(text)

class Controle:

 def tesseract_opc(self,ops,path):
    img = cv2.imread(path)
    if ops is 0:
      print("Placa:{0}".format(pytesseract.image_to_string(img)))
    elif ops is 1:
      # OR explicit beforehand converting
      ocr = pytesseract.image_to_string(Image.fromarray(img),lang='eng')
      print(ocr)
    elif ops is 1:
      # Get verbose data including boxes, confidences, line and page numbers
      print(pytesseract.image_to_data(Image.open('test.png')))
    elif ops is 2:
      # Get information about orientation and script detection
      print(pytesseract.image_to_osd(Image.open('test.png')))
    else:
      print("Opcao Invalida")






 def tesseract_pdf(self,ops):
    if ops is 0:
      # get a searchable PDF
      pdf = pytesseract.image_to_pdf_or_hocr('Placa.jpg', extension='pdf')
    else:
      # get HOCR output
      hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

#obj = Controle()
#obj.tesseract_opc(0)
