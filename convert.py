import argparse
import sys
import os
from PIL import Image
import numpy as np
import TXTtoBits
import encodeInBMP

parser = argparse.ArgumentParser()

parser.add_argument('-v', "--verbose", help="Verbose mode", action="store_true")
parser.add_argument('-n', '--number', help="Number of files to code", type=int)
parser.add_argument('-i', '--image', help="Address of the image to code", type=str)
parser.add_argument('-o', '--output', help="Output address of the encoded image", type=str)
parser.add_argument('-t', '--text', help='Address of the text to code', type=str)
parser.add_argument('-f', '--file', help="Address of the file once decodec", type=str)

args = parser.parse_args()

if args.number <= 0:
    print("Number of files has to be at least equal to 1.")
    sys.exit(1)

if (args.image[-4:].lower() != '.jpg' and args.image[-4:].lower() != '.png' and args.image[-4:].lower() != '.bmp'
        and args.image[-4:].lower() != '.xmp'):
    print("Error : Origin file is not an image.")
    sys.exit(1)

if args.output[-4:].lower() != '.bmp':
    print("Error : Output image is not a bitmap image.")
    sys.exit(1)

if args.verbose:
    print('Opening files...\n')

if not (os.path.exists(args.image)):
    print("Error : One of the specified files does not exist.")
    sys.exit(1)

imgArray = np.array(Image.open(args.image))
output = args.output
number = args.number
file = args.file
text = args.text

textlist = text.split(',')
filelist = file.split(',')


if len(textlist) != number or len(filelist) != number:
    print("Error : The number of texts and/or the number of output file is not equal to number.")
    sys.exit(1)

for textname in textlist:

    if textname[-4:].lower() != '.txt':
        print("Error : text has to be at .txt format.")
        sys.exit(1)

    if not (os.path.exists(textname)):
        print("Error : One of the specified files does not exist.")
        sys.exit(1)

if args.verbose:
    print('Converting text to binary...\n')

bitText = TXTtoBits.convertToBits(textlist, filelist)

if args.verbose:
    print("Coding the message in the image...\n")

imgArray = encodeInBMP.encode(imgArray, bitText)

if args.verbose:
    print("Saving the image...\n")

img = Image.fromarray(imgArray)

img.save(output)

print("Encoded image has been saved in the following file : {} !".format(output))
sys.exit(0)
