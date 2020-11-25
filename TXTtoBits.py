import codecs

def convertToBits(textlist,filelist):

    bitNumber = bin(len(textlist))[2:].zfill(8)
    bitList = [bitNumber]
    for i in range(len(textlist)):
        text = open(textlist[i], 'r')
        line = text.readline()
        listTEXT = []
        bitFile = bin(int((filelist[i].encode('utf-8')).hex(), 16))[2:]
        bitEndFile = bin(int(("ENDFILE".encode('utf-8')).hex(), 16))[2:]
        while line:
            listTEXT.append(line)
            line = text.readline()
        ftext = ''.join(listTEXT)
        bitText = bin(int((ftext.encode('utf-8')).hex(), 16))[2:]
        bitEndText = bin(int(("ENDTEXT".encode('utf-8')).hex(), 16))[2:]
        bitList.append(bitFile+bitEndFile+bitText+bitEndText)
        bitList.insert(0, bin(int(str(len(''.join(bitList)) + 64)))[2:].zfill(64))
    return (''.join(bitList))


def convertToString(bin_st): #bin_st est un string du type '001011011110'

    hexa = hex(int(bin_st, 2))[2:]
    text = codecs.decode(hexa, 'hex').decode('utf-8')
    return(text)