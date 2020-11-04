def encode(img, bitText): #img est de type np.array

    listBitText = list(str(bitText))
    listBitText.append(list(str(100010101001110010001000100001101001111010001000100010101001000010001010101001001000101))) #code d'arrêt (en clair ENDCODEHERE)
    listValues = []
    for line in img:
        for pixel in line:
            for value in pixel:
                value = bin(int(value))[2:]
                listValues.append(value)

    for i in range(len(listBitText)):
        l = list(str(listValues[i]))
        l[-1] = listBitText[i]
        listValues[i] = int(''.join(l))

    for line in img:
        for pixel in line:
            for value in pixel:
                try:
                    value = int(listValues[0], 2)
                    del(listValues[0])
                except:
                    return img








