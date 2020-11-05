def split(bintext):
    
    keyword="1000101010011100100010001000110010010010100110001000101" # random binary word
    addr_out=""
    message=""
    
    dest=True
    
    for i in bintext:
        keyword=keyword[1:]+i
        if keyword=="1000101010011100100010001000110010010010100110001000101": # binary ENDFILE
            dest=False
        if dest:
            addr_out+=i
        else:
            message+=i
            if keyword=="1000101010011100100010001010100010001010101100001010100": # binary ENDTEXT
                return addr_out, message
    
    return addr_out, message