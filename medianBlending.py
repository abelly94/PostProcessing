
import numpy as np
import PIL
import os


#BASE_DIR = "C:/"


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
    photo.close()
    return pixels


def get_median_values(pic_arrays):
    mixed_array = np.stack(pic_arrays, axis=3)
    medians = np.median(mixed_array, 3)
    final_pixels = medians.astype('uint8', casting='unsafe', copy=False)
    return final_pixels


def make_new_photo(pixel_array, targetdir):
    image_path = os.path.join(targetdir,"medianBlended.JPG")
    newpic = PIL.Image.fromarray(pixel_array)
    newpic.save(image_path, quality=90)
    return()


def blend_pics():
    # find all pictures in selected directory
    mydir = raw_input("Where are the pictures located")
    pictures = get_file_list(mydir)

    # gather all of the picture arrays
    pic_arrays = []
    for pic in pictures:
        pixels = process_picture(pic)
        pic_arrays.append(pixels)

    # blend the pictures together by selecting the median pixel value
    blended = get_median_values(pic_arrays)

    make_new_photo(blended)
