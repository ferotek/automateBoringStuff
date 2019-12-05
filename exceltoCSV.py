
import csv, os, openpyxl

os.makedirs('convert', exist_ok=True)

for excelFile in os.listdir('.'):
	if excelFile[-4:] == 'xlsx':

		wb = openpyxl.load_workbook(excelFile)
		csvName = excelFile[:-5] + '.csv'
		csvOutput = open(os.path.join('convert', csvName), 'w', newline='')

		for sheetName in wb.sheetnames:
			sheet = wb[sheetName]
			csvWriter = csv.writer(csvOutput)

			for rowNum in range(1, sheet.max_row + 1):
				rowData = []
				for colNum in range(1, sheet.max_column + 1):
					rowData.append(sheet.cell(row=rowNum, column=colNum).value)
				csvWriter = csv.writer(csvOutput)
				csvWriter.writerow(rowData)
		csvOutput.close()

    # Skip non-xlsx files, load the workbook object.
	    
	        # Loop through every sheet in the workbook.
	        
