

import csv, os

os.makedirs('removeheader', exist_ok=True)

i = 0


for fileName in os.listdir('.'):
    if fileName[-3:] == 'csv':
    
        
        csvFileObj = open(fileName)
        readerObj = csv.reader(csvFileObj)
        csvOutput = open(os.path.join('removeheader', fileName), 'w', newline='')
        for row in readerObj:
            if readerObj.line_num != 1: 
                csvWriter = csv.writer(csvOutput)
                csvWriter.writerow(row)

        csvFileObj.close()

   

