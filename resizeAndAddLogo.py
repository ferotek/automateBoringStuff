import os
from PIL import Image

catLogo = Image.open('/Users/davidguo/Documents/Pythom/automate_online-materials/catlogo.png')
logowidth, logoheight = catLogo.size

sqsize = 300

for img in os.listdir('.'):
	if img[-3:] == 'png' or img[-3:] == 'jpg':
		impose = Image.open(img)
		width, height = impose.size
		if width > sqsize and height > sqsize:
			if height > width:
				height = int((sqsize / width) * height)
				width = sqsize
				impose = impose.resize((width, height))
			else:
				width = int((sqsize / height) * width)
				height = sqsize
				impose = impose.resize((width, height))

		impose.paste(catLogo, (width - logowidth, height - logoheight), catLogo)
		impose.save('pasted.png')



