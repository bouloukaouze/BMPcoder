import codecs

def convertToBits(text, file):

    line = text.readline()
    listTEXT = []
    listTEXT.append(file+'ENDFILE')
    while line:
        listTEXT.append(line)
        line = text.readline()
    listTEXT.append('ENDTEXT')
    ftext = ''.join(listTEXT)
    bitText = bin(int((ftext.encode('utf-8')).hex(), 16))[2:]
    return(bitText)

def convertToString(bin_st): #bin_st est un string du type '0b001011011110'

    hexa = hex(int(bin_st[2:], 2))[2:]
    text = codecs.decode(hexa, 'hex').decode('utf-8')
    return(text)

