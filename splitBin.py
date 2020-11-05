def split(bintext):
    
    keyword = "1000101010011100100010001000110010010010100110001000110" # random binary word
    addr_out = ""
    message = ""
    
    dest = True
    
    for i in bintext[2:]:
        keyword = keyword[1:]+i
        if dest:
            addr_out += i
            if keyword == "1000101010011100100010001000110010010010100110001000101": # binary ENDFILE
                dest = False
                addr_out = addr_out[:-55] # on vire les bits de ENDFILE
        else:
            message += i
            if keyword == "1000101010011100100010001010100010001010101100001010100": # binary ENDTEXT
                message = message[:-55] # on vire les bits de ENDTEXT
                return addr_out, message
    
    return addr_out, message