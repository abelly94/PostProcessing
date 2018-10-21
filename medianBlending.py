
import numpy
import PIL
import os


BASE_DIR = r'F:/WASA pics/IOL/Camera 2/median and layer testing/'

red_band = []
green_band = []
blue_band = []


def get_file_list(dir):
    files = []
    for pic in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,pic)):
            files.append(pic)
        else:
            pass
    return(files)


def primaryPicture(path):
    pic = PIL.Image.open(path)
    w,h = pic.size
    pixLocation = [(y,x) for x in range(h) for y in range(w)]
    bands = pic.getdata()
    for pixel in bands:
        red_band.append([pixel[0]])
        green_band.append([pixel[1]])
        blue_band.append([pixel[2]])
    pic.close()
    return()


def add_bands(picPath):
    mypath = os.path.join(BASE_DIR,picPath)
    pic = PIL.Image.open(mypath)
    w,h = pic.size
    if (w*h) == len(red_band):
        pass
    else:
        print("This picture is a different size, it can not be blended with the primary photo")
        return()
    bands = pic.getdata()
    for i,pixel in enumerate(bands):
        red_band[i].append(pixel[0])
        green_band[i].append(pixel[1])
        blue_band[i].append(pixel[2])
    return()


def median_pixels(red,green,blue):
    corrected_pixels = []
    for i in xrange(len(red)):
        r = numpy.median(red[i])
        g = numpy.median(green[i])
        b = numpy.median(blue[i])
        corrected_pixels.append((r,g,b))
    return corrected_pixels


def make_new_photo(pixels):
    image_path = os.path.join(BASE_DIR,"medianBlended.JPG")
    newpic = PIL.Image.new("RGB",(5120,3840))
    newpic.putdata(pixels)
    newpic.save(image_path)
    print("enhanced photo saved at {0}".format(image_path))
    return()


def mainloop():
    pixLocation = []

    # get all of the pictures in the directory
    pictures = []
    for pic in os.listdir(BASE_DIR):
        pic_path = os.path.join(BASE_DIR,pic)
        pictures.append(pic_path)

    first_pic = pictures.pop(0)
    primaryPicture(first_pic)

    for path in pictures:
        add_bands(path)

    new_colors = median_pixels(red_band,green_band,blue_band)

    make_new_photo(new_colors)