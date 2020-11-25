def getNumber(bintext):

    return(int(bintext[:8], 2))

def split(bintext, number):

    addr_out_list = []
    message_list = []

    for k in range(number):
        keyword = "0000101010011100100010001001110010010010100110001000110"
        addr_out = ""
        message = ""
    
        dest = True

        count = -1
        for i in bintext:
            count += 1
            keyword = keyword[1:]+i
            if dest:
                addr_out += i
                if keyword == "1000101010011100100010001000110010010010100110001000101": # binary ENDFILE
                    dest = False
                    addr_out_list.append(addr_out[:-55]) # on vire les bits de ENDFILE
            else:
                message += i
                if keyword == "1000101010011100100010001010100010001010101100001010100": # binary ENDTEXT
                    message_list.append(message[:-55]) # on vire les bits de ENDTEXT
                    bintext = bintext[count:]
                    break

    
    return addr_out_list, message_list