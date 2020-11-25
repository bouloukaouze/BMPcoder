def gettext(img, verbose):

    """
    Takes image with encoded message and returns binary text
    """

    bitNumber = ""

    countNumber = 0

    for line in img:
        for pixel in line:
            for value in pixel:
                countNumber += 1
                bitNumber += str(bin(int(value))[-1])
                if countNumber == 64:
                    break
            if countNumber == 64:
                break
        if countNumber == 64:
            break

    bitNumber = int(bitNumber, 2)

    message = ""

    count = 0

    for line in img:
        for pixel in line:
            for value in pixel:
                count += 1
                if verbose and count%100000 == 0:
                    print('Read '+str(count)+' bits...')
                message += str(bin(int(value))[-1])
                if count == bitNumber:
                    if verbose:
                        print('Read ' + str(count) + ' bits !\n')
                    return message