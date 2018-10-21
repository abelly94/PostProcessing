
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
    picture_arrays.append(pixels)
    photo.close()


def get_median_values(pic_arrays):
    mixed_array = np.stack(pic_arrays, axis=3)
    medians = np.median(mixed_array, 3)
    final_pixels = medians.astype('uint8', casting='unsafe', copy=False)
    return final_pixels


def make_new_photo(pixel_array):
    image_path = os.path.join(BASE_DIR,"medianBlended.JPG")
    newpic = PIL.Image.fromarray(pixel_array)
    newpic.save(image_path, quality=90)
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