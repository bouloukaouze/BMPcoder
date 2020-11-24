def encode(img, bitText): #img est de type np.array.

    for line in img:
        for pixel in line:
            for i in range(len(pixel)):
                try:
                    value = bin(int(pixel[i]))[2:]
                    listBit = list(bitText)
                    listVal = list(value)
                    listVal[-1] = listBit[0]
                    value = int(''.join(listVal), 2)
                    pixel[i] = value
                    bitText = ''.join(listBit[1:])
                except:
                    return img