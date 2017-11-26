from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-s', '--size', help='size of image. e.g. 20x40. ', required=True)
parser.add_argument('-f', '--file', help='path to the image to be resized. ', required=True)
args = parser.parse_args()

file = args.file

width, height = args.size.split("x")
filename, file_extension = os.path.splitext(file)

print("Size of destination image is: " + str(width) + " x " + str(height));

# Read the original image
originalImage = Image.open(file)

for i in range(1, 4):
    # Get new size for the image
    newWidth  = int(width) * i
    newHeight = int(height) * i

    # construct new image file name
    newImageName = filename + "@"+str(i)+"x" + file_extension

    # Options are ANTIALIAS, BICUBIC, NEAREST, ANTIALIAS
    # linear interpolation in a 2x2 environment
    newImage = originalImage.resize((newWidth, newHeight), Image.ANTIALIAS)   
    newImage.save( newImageName )

    print(" - Saved image: " + newImageName)


