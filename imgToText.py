def gettext(img):
    
    """
    Takes image with encoded message and returns 
    """
    
    addr_out=""
    message=""
    text=False
    keyword="1000101010011100100010001000110010010010100110001000111" # binary keyword
    
    for line in img:
        for pixel in line:
            for value in pixel:
                bit=str(bin(int(value))[-1])
                if not text:
                    addr_out+=bit
                else:
                    message+=bit
                keyword=keyword[1:]+bit
                if keyword=="1000101010011100100010001000110010010010100110001000101": # binary "ENDFILE"
                    text=True
                if keyword=="1000101010011100100010001010100010001010101100001010100": # binary "ENDTEXT"
                    return (addr_out, message)