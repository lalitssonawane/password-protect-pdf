from pypdf import pdffilewriter , pdffilereader
import getpass
pdfwriter = pdfFileWriter()
pdf = pdfFileReader("l.pdf")
for page_num in range (pdf.numPages):
    pdfwriter.addpage(pdf.getPage(page_num))
passw=getpass.getpass(prompt='Enter Password: ')
pdfWriter.ecrypt(passw)
with open('ho.pdf','wb') as f:
    pdfwriter.write(f)