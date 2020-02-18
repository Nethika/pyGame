import os
from PIL import Image

input_path = "fish-bowl.png"
print("   " + input_path)
input_img = Image.open(input_path)

image_width =100
# calculate image height
input_width = input_img.width
input_height = input_img.height
factor = input_height / input_width 
image_height = int(factor * image_width)



# resize
img = input_img.resize((image_width, image_height), Image.ANTIALIAS)

#fix orientation
if hasattr(input_img, '_getexif'):
    orientation = 0x0112
    exif = input_img._getexif()
    if exif is not None:
        orientation = exif[orientation]
        rotations = {
            3: Image.ROTATE_180,
            6: Image.ROTATE_270,
            8: Image.ROTATE_90
        }
        if orientation in rotations:
            img= img.transpose(rotations[orientation])
        

# save
filename = "fish-bowl-small.png"
img.save(filename, quality=100)