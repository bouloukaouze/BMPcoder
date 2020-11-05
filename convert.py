import JPGtoBMP
import argparse
import sys
import os
from PIL import Image
import numpy as np
import TXTtoBits
import encodeInBMP

parser = argparse.ArgumentParser()

parser.add_argument('-v', "--verbose", help="Mode verbeux", action="store_true")
parser.add_argument('-i', '--image', help="Adresse de l'image à coder", type=str)
parser.add_argument('-o', '--output', help="Adresse de sortie de l'image codée", type=str)
parser.add_argument('-t', '--text', help='Adresse du texte à coder', type=str)
parser.add_argument('-f', '--file', help="Nom du fichier une fois décodé.", type=str)

args = parser.parse_args()

if (args.image[-4:].lower() != '.jpg' and args.image[-4:].lower() != '.png' and args.image[-4:].lower() != '.bmp'
    and args.image[-4:].lower() != '.xmp'):
    print("Erreur : Le fichier d'origine n'est pas une image.")
    sys.exit(1)

if (args.output[-4:].lower() != '.jpg' and args.output[-4:].lower() != '.png' and args.output[-4:].lower() != '.bmp'
    and args.output[-4:].lower() != '.xmp'):
    print("Erreur : Le fichier de sortie n'est pas une image.")
    sys.exit(1)

if args.text[-4:].lower() != '.txt':
    print("Erreur : le texte doit être au format .txt")
    sys.exit(1)

if not(os.path.exists(args.image), os.path.exists(args.output), os.path.exists(args.text)):
    print("Erreur : un des fichiers spécifiés n'existe pas.")
    sys.exit(1)

if args.verbose:
    print('Ouverture des fichiers...\n')

imgArray = np.array(Image.open(JPGtoBMP.convertToBMP(args.image)))
output = args.file+"ENDFILE"+args.output+"ENDTEXT"
text = open(args.text, 'r')

if args.verbose:
    print('Conversion du texte en binaire...\n')

bitText = TXTtoBits.convertToBits(text)

if args.verbose:
    print("Encodage du message dans l'image...\n")

imgArray = encodeInBMP.encode(imgArray, bitText)

if args.verbose:
    print("Sauvegarde de l'image...\n")

img = Image.fromarray(imgArray)

img.save(output)

print("L'image codée a bien été sauvegardée dans le fichier {}".format(output))

sys.exit(0)


