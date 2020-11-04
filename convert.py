import JPGtoBMP
import argparse
import sys
import os
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-v', "--verbose", help="Mode verbeux",
                    action="store_true")

parser.add_argument('-f', '--file', help="Adresse de l'image à coder", type=str)
parser.add_argument('-o', '--output', help="Adresse de sortie de l'image codée", type=str)
parser.add_argument('-t', '--text', help='Adresse du texte à coder', type=str)
args = parser.parse_args()

if (args.file[-4:].lower() != '.jpg' and args.file[-4:].lower() != '.png' and args.file[-4:].lower() != '.bmp'
    and args.file[-4:].lower() != '.xmp'):
    print("Erreur : Le fichier d'origine n'est pas une image.")
    sys.exit(1)

if (args.output[-4:].lower() != '.jpg' and args.output[-4:].lower() != '.png' and args.output[-4:].lower() != '.bmp'
    and args.output[-4:].lower() != '.xmp'):
    print("Erreur : Le fichier de sortie n'est pas une image.")
    sys.exit(1)

if args.text[-4:].lower() != '.txt':
    print("Erreur : le texte doit être au format .txt")
    sys.exit(1)

if not(os.path.exists(args.file), os.path.exists(args.output), os.path.exists(args.text)):
    print("Erreur : un des fichiers spécifiés n'existe pas.")
    sys.exit(1)

file = np.array(Image.open(JPGtoBMP.convertToBMP(args.file)))
output = args.output
text = open(args.text, 'r')
