import PIL
import numpy as np

def encode(img, bitText): #img est de type np.array

    listBitText = list(str(bitText))
    listBitText.append(list(str(100010101001110010001000100001101001111010001000100010101001000010001010101001001000101))) #code d'arrêt
    listValues = []
    for pixel in img:
        for value in pixel:
            value = bin(int(value))[2:]
            listValues.append(value)

    for i in range(len(listBitText)):
        l = list(str(listeValues[i]))
        l[-1] = listBitText[i]
        listeValues[i] = int(''.join(l))








