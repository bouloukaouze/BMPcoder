def split(bintext):
    
    keyword="KEYWORD"
    addr_out=""
    message=""
    
    dest=True
    
    for i in bintext:
        keyword=keyword[1:]+i
        if keyword=="ENDFILE":
            dest=False
        if dest:
            addr_out+=i
        else:
            message+=i
            if keyword=="ENDTEXT":
                return addr_out, message
    
    return addr_out, message