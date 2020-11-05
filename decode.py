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
    print("Erreur : Le fichier d'origine n'est pas une image bitmap.")
    sys.exit(1)
    
if not(os.path.exists(args.image)):
    print("Erreur : le fichier spécifié n'existe pas.")
    sys.exit(1)

if args.verbose:
    print("Opening file...\n")

imgArray = np.array(Image.open(args.image))

if args.verbose:
    print("Extracting message from image...\n")

bintext = imgToText.gettext(imgArray)

if args.verbose:
    print("Converting message to clear text...\n")
    

addr_out, message = splitBin.split(bintext)
addr_out, message = TXTtoBits.convertToString(addr_out), TXTtoBits.convertToString(message)

out_file = open(addr_out, 'w')
out_file.write(message)
out_file.close()