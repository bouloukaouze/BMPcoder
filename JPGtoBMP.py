from PIL import Image

def convertToBMP(file): #file est un string du type "name.jpg"

    img = Image.open(file)
    img = img.save('%s.bmp' % file[:-4])

    return('%s.bmp' % file[:-4])