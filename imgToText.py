def gettext(img):
    
    """
    Takes image with encoded message and returns binary text
    
    PROBLEM : DOES NOT DETECT WORDS ENDFILE NOR ENDTEXT
    """
    
    addr_out=""
    message=""
    text=False
    keyword="1000101010011100100010001000110010010010100110001000101" # binary keyword
    
    v=0
    
    for line in img:
        for pixel in line:
            for value in pixel:
                if v%10000==0:
                    print("v = ", v, " and value = ", value)
                if v==img.size-1:
                    print("v = ", v, " and value = ", value)
                v+=1
                bit=str(bin(int(value))[-1])
                if not text:
                    addr_out+=bit
                else:
                    message+=bit
                keyword=keyword[1:]+bit
                if keyword=="1000101010011100100010001000110010010010100110001000101": # binary "ENDFILE"
                    print("ENDFILE")
                    text=True
                if keyword=="1000101010011100100010001010100010001010101100001010100": # binary "ENDTEXT"
                    print("ENDTEXT")
                    return (addr_out, message)