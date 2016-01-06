from __future__ import print_function
from PIL import Image
import glob
import os

os.chdir("./")
allfiles = glob.glob("*.png")

for file in allfiles:

	p1 = file.rfind(' ')
	p2 = file.rfind('x')
	p3 = file.rfind('.')

	if p1==-1 or p2==-1 or p3==-1:
		continue

	# Get width and height to your needs
	width = int(file[p1:p2])
	height = int(file[p2+1:p3])

	print("\nFound Image '" + file + "'" )
	print("Size of destination image is: " + str(width) + " x " + str(height));
	# Read the original image
	originalImage = Image.open(file)

	for i in range(1,4):
		# Get new size for the image
		newWidth  = width * i
		newHeight = height * i

		# construct new image file name
		newImageName = file[:p1];
		if i==1:
			newImageName = newImageName + ".png"
		else: 
			newImageName = newImageName + "@"+str(i)+"x.png"

		# Options are ANTIALIAS, BICUBIC, NEAREST, ANTIALIAS
		newImage = originalImage.resize((newWidth, newHeight), Image.ANTIALIAS)     # linear interpolation in a 2x2 environment
		newImage.save( newImageName )

		print( " - Image '" + newImageName + "' is saved" )

	print("\n");

