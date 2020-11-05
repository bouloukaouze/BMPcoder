def gettext(img):
    
    """
    Takes image with encoded message and returns binary text
    """
    
    message = ""
    
    for line in img:
        for pixel in line:
            for value in pixel:
                message += str(bin(int(value))[-1])

    return message