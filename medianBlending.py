
import numpy as np
from PIL import Image
import os


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
    photo = Image.open(filename)
    pixels = np.array(photo)
    photo.close()
    return pixels


def get_median_values(pic_arrays):
    mixed_array = np.stack(pic_arrays, axis=3)
    medians = np.median(mixed_array, 3)
    final_pixels = medians.astype('uint8', casting='unsafe', copy=False)
    return final_pixels


def make_new_photo(pixel_array, targetfile):
    image_path = targetfile
    newpic = Image.fromarray(pixel_array)
    newpic.save(image_path, quality=90)
    newpic.close()
    return()


def blend_pics(file_list):

    # gather all of the picture arrays
    pic_arrays = []
    for pic in file_list:
        pixels = process_picture(pic)
        pic_arrays.append(pixels)

    # blend the pictures together by selecting the median pixel value
    blended = get_median_values(pic_arrays)

    return blended


def make_batch(directory):

    batchsize = int(raw_input("Enter the batching size "))

    # create a sorted file list from the directory
    full_file_list = get_file_list(directory)
    full_file_list.sort()
    print("there are {0} files in the directory".format(len(full_file_list)))

    # break list into list of lists with len batchsize
    batch = []
    batch_list = []
    for filename in full_file_list:
        batch.append(filename)
        if len(batch) == batchsize:
            batch_list.append(batch)
            batch = []
        else:
            pass

    if len(batch) > 0:
        batch_list.append(batch)
    return batch_list


if __name__ == '__main__':
    mydir = raw_input("Enter the picture directory ")
    mybatches = make_batch(mydir)
    print("there are {0} batches to process".format(len(mybatches)))
    counter = 0
    for batch in mybatches:
        print("processing batch {0} now".format(counter))
        newpic = blend_pics(batch)
        basename = "blended {0}.JPG".format(counter)
        filepath = os.path.join(mydir, 'blended' , basename)
        make_new_photo(newpic, filepath)
        counter += 1
