from __future__ import print_function
from PIL import Image
import glob
import os

os.chdir("./")
allfiles = glob.glob("*.png")

directories = ["ldpi", "mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
resizes = [0.75, 1, 1.5, 2, 3, 4]

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

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

	for i in range(0, 6):
		# Get new size for the image
		newWidth  = int(width * resizes[i])
		bewHeight = int(height * resizes[i])

		# construct new image file name
		newImageName = directories[i] + "/" + file[:p1] + ".png"
		
		# Options are ANTIALIAS, BICUBIC, NEAREST, ANTIALIAS
		newImage = originalImage.resize((newWidth, newWidth), Image.ANTIALIAS)
		newImage.save( newImageName )

		print( " - Image '" + newImageName + "' is saved" )

	print("\n");

