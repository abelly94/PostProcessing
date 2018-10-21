
import numpy as np
import PIL
import os


#BASE_DIR = "C:/"

red_band = []
green_band = []
blue_band = []

picture_arrays = []


def get_file_list(projectdir):
    files = []
    for pic in os.listdir(projectdir):
        fullpath = os.path.join(projectdir, pic)
        if os.path.isfile(fullpath):
            files.append(fullpath)
        else:
            pass
    return files


def process_picture(filename):
    try:
        photo = PIL.Image.open(filename)
    except:
        print("There was an issue with file {0}".format(filename))
    pixels = np.array(photo)
    picture_arrays.append(pixels)
    photo.close()


def get_median_values(pic_arrays):
    mixed_array = np.stack(pic_arrays, axis=3)
    medians = np.median(mixed_array, 3)
    final_pixels = medians.astype('uint8', casting='unsafe', copy=False)
    return final_pixels


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