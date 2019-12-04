import PyPDF2, os

path = '/Users/davidguo/Documents/Pythom/'

dirs = os.listdir( path )

listpdf = []

for file in dirs:

	if file[-3:] == 'pdf':

		
		listpdf.append(file)

listpdf.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for i in range(len(listpdf)):
	print(listpdf[i])
	if i == 0:
		pdf1File = open(listpdf[i], 'rb')
		pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
		for pageNum in range(pdf1Reader.numPages):
			pageObj = pdf1Reader.getPage(pageNum)
			pdfWriter.addPage(pageObj)
	
	else:
		pdf1File = open(listpdf[i], 'rb')
		pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
		for pageNum in range(1, pdf1Reader.numPages):
			pageObj = pdf1Reader.getPage(pageNum)
			pdfWriter.addPage(pageObj)
	

pdfOutputFile = open('/Users/davidguo/Documents/Pythom/pdfs/combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()


