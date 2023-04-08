import pyttsx3
import PyPDF4
book = open('oop.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(9, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()