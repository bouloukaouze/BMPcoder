import argparse
import sys
import os
from PIL import Image
import numpy as np
import imgToText
import TXTtoBits
import splitBin

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbose', help="Mode verbeux", action="store_true")
parser.add_argument('-i', '--image', help="Address of image to decode", type=str)
args = parser.parse_args()

if args.image[-4:].lower() != '.bmp':
    print("Error : Origin file is not a bitmap image.")
    sys.exit(1)
    
if not(os.path.exists(args.image)):
    print("Error : specified file does not exist.")
    sys.exit(1)

if args.verbose:
    print("Opening file...\n")

imgArray = np.array(Image.open(args.image))

if args.verbose:
    print("Extracting message from image...\n")

bintext = imgToText.gettext(imgArray, args.verbose)[64:]

if args.verbose:
    print("Converting message to clear text...\n")

addr_out_list, message_list = splitBin.split(bintext[8:], splitBin.getNumber(bintext))

for i in range(len(addr_out_list)):
    addr_out, message = TXTtoBits.convertToString(addr_out_list[i]), TXTtoBits.convertToString(message_list[i])

    if args.verbose:
        print("Writing text on %s...\n" % addr_out)

    out_file = open(addr_out, 'w')
    out_file.write(message)
    out_file.close()

    print('Done !\n')
    
sys.exit(0)