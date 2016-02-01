# svg2drawable.py

### Abstract

This script renders .svg files into .png files in the correct resolution for Android.
The output .png files will be rendered into their corresponding directories, i.e
*res/drawable-**X**dpi/output.png* in the current working directory.

Tested this script on Arch Linux 02/jan/2015, Ubuntu and Windows. 

**Depends on InkScape for rendering!**

## Usage

**svg2drawable** *input file* *output file* --width px --height px

### Examples

Render the file "vector-logo.svg" into "logo.png" with the width 200px (height will be kept relative).
```
svg2drawable vector-logo.svg logo.png --width 200 
```
Render the file "vector-splash-screen.svg" into "splash-screen.png" with the height 640px (width will be kept relative).
```
svg2drawable vector-splash-screen.svg splash-screen.png --height 640 
```
Render the file "vector-button.svg" into "button.png" with the height 64px and width 48px.
```
svg2drawable vector-button.svg button.png --height 64 --width 48
```
Render all svg files into png files with the height 64px.
```
svg2drawable *.svg --height 64
```
Render all svg files into png files with the height 64px, and removes all surrounding whitespaces.
```
svg2drawable *.svg --height 64 --no_padding
```
Licenced under GPL-3 License.
