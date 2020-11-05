import codecs

def convertToBits(text, file):

    line = text.readline()
    listBITS = []
    listBITS.append(bin(int((file.encode('utf-8')).hex(), 16))[2:])
    listBITS.append(bin(int(('ENDFILE'.encode('utf-8')).hex(), 16))[2:])
    while line:
        lineUTF = line.encode('utf-8')
        lineHEX = lineUTF.hex()
        lineBITS = bin(int(lineHEX, 16))[2:]
        listBITS.append(lineBITS)
        line = text.readline()
    bitText = '1010'.join(listBITS)
    listBITS.append(bin(int(('ENDTEXT'.encode('utf-8')).hex(), 16))[2:])
    return(bitText)

def convertToString(bin): #bin est un string du type '0b001011011110'

    hexa = hex(int(bin[2:], 2))[2:]
    text = codecs.decode(hexa, 'hex').decode('utf-8')
    return(text)

