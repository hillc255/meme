import typing
from typing import Optional
from PIL import Image, ImageDraw, ImageFont
import os
import random
from random import randint
import textwrap

#class for the memeengine
class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    #method
    def make_meme(self, img_path: str, body: str, author: str, width=500) -> Optional[str]:
        # loads the image from the imgPath, creating an in-memory represtation of the image
        img: Image.Image = Image.open(img_path, mode='r')
        print(f"img: ",img)
        print(f"body: ",body)
        print(f"author: ",author)

        # create a destination path for the meme

        outputFile_name = os.path.join(self.output_dir, 
            f'meme_{random.randint(0,100000000)}.png')

        print(f"OUTPUTFILE_NAME:  {outputFile_name}")

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        # Add text and author test to the image
        message = (str(body) + " - "+ str(author))
        print(f"message: ", message)

        if message is not None:
            draw = ImageDraw.Draw(img)

            ttfFile = os.path.join(
                    os.path.dirname(__file__),
                    'fonts/LilitaOne-Regular.ttf'
                )
                
            font = ImageFont.truetype(ttfFile, size=30)

            #wrapped message by message char length
            message = textwrap.fill(text=message, width=20)

            #generate random x,y coordinates
            draw.text(((random.randint(10,250)), (random.randint(10,250))), message, font=font, fill='white')

        print("After message and ImageDraw")

        # save the meme to the dest path
        img.save(outputFile_name)

        print("Saved image")

        return os.path.abspath(outputFile_name)
        

#Requirements:
#The project defines a MemeGenerator module with the following 
# responsibilities:

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


