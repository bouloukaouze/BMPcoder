def gettext(img):
    
    addr_out=""
    message=""
    text=False
    keyword="KEYWORD"
    
    for line in img:
        for pixel in line:
            for value in pixel:
                bit=str(bin(int(value))[-1])
                if not text:
                    addr_out+=bit
                else:
                    message+=bit
                keyword=keyword[1:]+bit
                if keyword=="ENDFILE":
                    text=True
                if keyword=="ENDTEXT":
                    return (addr_out, message)