#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 05:25:16 2019

@author: augustinmorieux
"""




# using the Python Image Library (PIL) to resize an image
# works with Python27 and Python32
from PIL import Image
import os
#files = os.listdir(".")
for i in range (9759,9797):

    image_file = "./data_anime/1/"+str(i)+".png" #13.jpg"
    #image_file = filename
    #im = Image.open("./data_Basquiat/1/47.png")
    #rgb_im = im.convert('RGB')
    #rgb_im.save('47.jpg')
    #image_file = "./data_Basquiat/1/47.jpg" #13.jpg"

    img_org = Image.open(image_file)
# get the size of the original image
    width_org, height_org = img_org.size

    width = 500
    height = 420
# best down-sizing filter
    img_anti = img_org.resize((width, height), Image.ANTIALIAS)
# split image filename into name and extension
    name, ext = os.path.splitext(image_file)
# create a new file name for saving the result
    new_image_file = "%s%s" % (name,ext)
    img_anti.save(new_image_file)
    print("resized file saved as %s" % new_image_file)
# one way to show the image is to activate
# the default viewer associated with the image type
    import webbrowser
    webbrowser.open(new_image_file)





