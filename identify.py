import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/Users/davidguo/Documents/Pythom/automate_online-materials/catlogo.png'):

    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:

        # Check if file extension isn't .png or .jpg.
        if filename[-4:] == '.png' or filename[-4:] == '.jpg':
           

            imgfile = Image.open(os.path.join(foldername, filename))

            width, height = imgfile.size

            if width > 500 and height > 500:
            	numPhotoFiles += 1
            else:
            	numNonPhotoFiles += 1
            #continue    # skip to next filename

        # Open image file using Pillow.

		        # Check if width & height are larger than 500.


    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numNonPhotoFiles+numPhotoFiles > 0 and (numPhotoFiles)/(numNonPhotoFiles+numPhotoFiles) > 0.5:
        print(foldername)
