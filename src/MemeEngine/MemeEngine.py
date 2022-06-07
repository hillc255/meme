import typing
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

#class for the memeengine
class MemeEngine:
    def __init__(self, outPath):
        self.outPath = outPath

    #method
    def make_meme(self, imgPath: str, body: str, author: str) -> Optional[str]:
        # loads the image from the imgPath, creating an in-memory represtation of the image
        img: Image.Image = Image.open(imgPath)

        # create a destination path for the meme
        destPath = ''

        # Add body and author test to the image

        # save the meme to the dest path
        img.save(destPath)

        return destPath
        

#Requirements:
#The project defines a MemeGenerator module with the following responsibilities:

#Loading of a file from disk
#Transform image by resizing to a maximum width of 500px while maintaining the 
# input aspect ratio

#Add a caption to an image (string input) with a body and author to a random 
# location on the image.

#The class depends on the Pillow library to complete the defined, incomplete method 
# signatures so that they work with JPEG/PNG files.

#The method signature to make the meme should be: make_meme(self, img_path, text, 
# author, width=500) -> str #generated image path

#The init method should take a required argument for where to save the generated 
# images: __init__(self, output_dir...).


