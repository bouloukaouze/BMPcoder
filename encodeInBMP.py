def encode(img, bitText): #img est de type np.array

    listBitText = list(str(bitText))
    listValues = []
    for line in img:
        for pixel in line:
            for value in pixel:
                value = bin(int(value))[2:]
                listValues.append(value)

    for i in range(len(listBitText)):
        l = list(str(listValues[i]))
        l[-1] = str(listBitText[i])
        listValues[i] = int(''.join(l))

    for line in img:
        for pixel in line:
            for value in pixel:
                try:
                    value = int(listValues[0], 2)
                    del(listValues[0])
                except:
                    return img








