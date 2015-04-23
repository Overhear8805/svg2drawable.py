#!/usr/bin/python
#
# A simple script that render png images from svg files in the correct
# scale for Android drawables. Uses InkScape for rendering.
#
# Author: Simon Cedergren <dev@onyktert.nu>
# Run it at your own risk. This is my first Python script ever.
#
# ----------------------------------------------------------------------------
# The MIT License (MIT)
# 
# Copyright (c) 2015 Simon Cedergren 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------

import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("input_file", nargs=1, help="Name of the input_file file\(.svg\)")
parser.add_argument("output_file", nargs="?", help="Name of the output_file file\(.png\)")
parser.add_argument("--width", type=int, help="Desired width of the drawable \(mdpi\)")
parser.add_argument("--height", type=int, help="Desired height of the drawable \(mdpi\)")
args = parser.parse_args()

'''
 Check if either height or width was given as argument.
 If none was given - print error message and exit.
'''
has_enough_args = False
if args.height:
        has_enough_args = True
if args.width:
        has_enough_args = True
if not has_enough_args:
        print("ERROR: Missing argument: need at least width or height to run")
        exit()

'''
 Create the default folders that is used in Android 
 for drawables. These are created in the current 
 working directory.
 E.g. /res/drawable-mdpi/example.png
'''
def make_folders():
    dir_array = ["mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
    if not os.path.exists("res/"):
        for dir_name in dir_array:
            os.makedirs("res/drawable-"+dir_name)

def get_output_file():
    output_file = args.output_file if args.output_file else args.input_file[0]

    if output_file.endswith(".png"):
        return output_file
    elif output_file.endswith(".svg"):
        return output_file[:-4] + ".png"
    else:
        return output_file + ".png"

'''
 Render the image using InkScape.
 The images are rendered into .png files to their corresponding directory.
 their corresponding directory.
'''
def render_images():
    width = args.width
    height = args.height
    input_file = args.input_file[0]
    output_file = get_output_file()
    dir_array = ["mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
    res_array = [1, 1.5, 2, 3, 4]

    for index in range(len(dir_array)):
        print("Rendering " + dir_array[index]+"...")
        # If height is given; use height as the given argument to Inkscape.
        if height:
                y = int(height)*res_array[index]
                cmd = "inkscape {0}  --export-area-drawing -e res/drawable-{1} -h{2}".format(input_file, dir_array[index] +"/"+output_file, y)
        
        # If width is given; use width as the given argument to Inkscape.
        elif width:
                x = int(width)*res_array[index]
                cmd = "inkscape {0}  --export-area-drawing -e res/drawable-{1} -w{2}".format(input_file, dir_array[index] +"/"+output_file, x) 
        
        # If both width and height is given; use both.
        else:
                y = int(height)*res_array[index]
                x = int(width)*res_array[index]
                cmd = "inkscape {0}  --export-area-drawing -e res/drawable-{1} -w{2} -h{3}".format(input_file, dir_array[index] +"/"+output_file, x, y) 
       
        # Do the actual rendering
        subprocess.call(cmd.split(), shell=False) 
        print("\n")


# Run the code above.     
make_folders()
render_images()
