def convertToBits(text):

    line = text.readline()
    listBITS = []
    while line:
        lineUTF = line.encode('utf-8')
        lineHEX = lineUTF.hex()
        lineBITS = bin(int(lineHEX, 16))[2:]
        listBITS.append(lineBITS)
        line = text.readline()
    return(listBITS)

