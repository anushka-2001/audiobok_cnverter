import pyPDF2
from gtts import gTTS
pdfFileObj = open("Hector Garcia - Ikigai _ The Japanese Secret to a Long and Happy Life-Penguin Books (2017).pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)
pdfFileObj.close()

tts = gTTS(text=mytext, lang='en')
tts.save("story.mp3")