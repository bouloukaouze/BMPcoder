import argparse
import sys
import os
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbose', help="Mode verbeux", action="store_true")
parser.add_argument('-i', '--image', help="Address of image to decode", type=str)
args = parser.parse_args()

if (args.image[-4:].lower() != '.jpg' and args.image[-4:].lower() != '.png' and args.image[-4:].lower() != '.bmp' and args.image[-4:].lower() != '.xmp'):
    print("Erreur : Le fichier d'origine n'est pas une image.")
    sys.exit(1)
    
if not(os.path.exists(args.image)):
    print("Erreur : le fichier spécifié n'existe pas.")
    sys.exit(1)

if args.verbose:
    print("Opening file...\n")

imgArray = np.array(Image.open(args.image))
print(imgArray[0])

if args.verbose:
    print("Extracting message from image...\n")

