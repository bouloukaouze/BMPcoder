import codecs

def convertToBits(text):

    line = text.readline()
    listBITS = []
    while line:
        lineUTF = line.encode('utf-8')
        lineHEX = lineUTF.hex()
        lineBITS = bin(int(lineHEX, 16))[2:]
        listBITS.append(lineBITS)
        line = text.readline()
    bitText = list('1010'.join(listBITS))
    return(bitText)

def convertToString(bin): #bin est un string du type '0b001011011110'

    hex = hex(int(bin[2:], 2))
    text = codecs.decode(hex, 'hex').decode('utf-8')
    return(text)

