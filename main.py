import pyttsx3              
import PyPDF2               

book = open('Story.pdf', 'rb')                  
pdfReader = PyPDF2.PdfReader(book)              
pages = len(pdfReader.pages)                    
print('\033[1;32m Total pages in the book: ', pages)   

speaker = pyttsx3.init()                        

for num in range(0, pages):                    
    print('>>\033[1;32m Reading page No: ', num+1)       
    page = pdfReader.pages[num]
    text = page.extract_text()                  
    speaker.say(text)                           
    speaker.runAndWait()
