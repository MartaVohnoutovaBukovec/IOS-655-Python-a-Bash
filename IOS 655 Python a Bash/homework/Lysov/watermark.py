# image Klara jpeg watermark
# Marta Vohnoutova
# Here is a program - look at it, or even edit and try
# and send me the description what the Python program is doing
#
# Commented by A. Lysov
#
# This program will create copy of the .jpg images with watermark
# found in given directory and its subdirectories with names that include word
# _watermarked_ before extension .jpg
# Currently the watermark position is calculated using Title position of the image,
# however, if parameter 'scale' is passed, the watermark will be scaled to cover
# the entire image. If no .jpg files are found, then no work will be done and program
# will exit without displaying any message. The program allows to change the opacity
# of the waterwark, but both the location of the watermark and its opacity are hardcoded,
# rather than passed as parameters.
# If watermark file is in the same folder as images, its copy will be created.
# The resulting files have .jpeg extension as opposed to .jpg for the original files,
# so "double watermarking" of watermarked files never happens.
# The PIL library was initially developed for Python 2.x and in order for it to work
# with Python 3.x, Pillow package need to be installed.
# The program have been succesfully tested in Windows with Python 3.5 after Pillow installation

import os
import sys

# PIL is Python Image Library that is not avalable in Python 3
# To obtain this functionality install "Pillow" package in Python 3
# Since it is not standard library, we test if it was installed
try:
    from PIL import Image, ImageEnhance
except:
    print("Install Pillow to obtain PIL library.")


def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    # rases an exception of the following is false
    # not a very nice way to test input parameter
    # the default value passed here is 1, so we may be saved
    # from exception if passing nothing
    assert opacity >= 0 and opacity <= 1
    # we want to work only with RGBA type of image coding
    if im.mode != 'RGBA':
        # if not RGBA, convert to this standard
        # and change image pointer to converted image
        # so we do not change the original
        im = im.convert('RGBA')
    else:
        # if RGBA, create a copy in memory
        # and change image pointer to the copy of the image
        # so we do not change the original        
        im = im.copy()

    # obtain 'alpha' image from the entire image
    alpha = im.split()[3]
    # and enchance its britness and opacity
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    # replace original 'alpha' image with its enchanced version
    im.putalpha(alpha)
    #return enchanced image
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    # depending on our choice of opacity of watermark
    # we can reduce it, however this routine can throw an exception
    # if we have wrong value of opacity
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    # The image is converted to RGBA standard if it is not coded in RGBA
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    # if position is title, then mark is placed corresponding to title
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    # if we want to scale, watermark is scaled to the entire image
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, (im.size[0] - w, im.size[1] - h))
    # in default case the watermark is placed at the passed position
    else:
        layer.paste(mark, position)

    # composite the watermark with the layer    
    return Image.composite(layer, im, layer)


if __name__ == '__main__':
    
    # folder where images are located
    # kam="/home/marta/photostruk/klara"
    kam = "."
    # location of the image that is going to be used as watermark
    # vodoznak = "/home/marta/photostruk/logo/logo_ju.jpeg"
    vodoznak = "al.jpg"
    # position of the watermark on the original image
    position = "tile"
    # for all the files in initial folder and its subfolders
    for root, dirs, files in os.walk(kam):
        # for all files, but not directories
        for file in os.listdir(root):
            # if file extension is .jpg
            if file.endswith(".jpg"):
                # open file as an image
                im = Image.open(os.path.join(root, file))
                # open watermark as an image
                mark = Image.open(vodoznak)
                # add watermark to an image
                im_watermarked = watermark(im, mark, position, 0.15)
                # save image with watermark with name that includes "_watermarked_"
                im_watermarked.save(kam+"/" + file + "_watermarked_" + position + ".jpeg")
