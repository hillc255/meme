"""MemeEngine module provides MemeEngine class with methods to make a meme."""

from typing import Optional
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    """MemeEngine class to make a meme.

    Method parameters are to make the meme and save it to
    a given path.
    """

    def __init__(self, output_dir):
        """Init method with required output_dir argument to save the image.

        Argument:
        output_dir (str) : Required destination path to save the meme
        """
        self.output_dir = output_dir

    def make_meme(self, img_path: str, body: str,
                  author: str, width=500) -> Optional[str]:
        """Make_meme method signature to make the meme with required arguments.

        Arguments:
        img_path (str)   : Required path to load the image
        body (str)       : Required quote from QuoteModel
        author (str)     : Required author from QuoteModel
        width (int)      : Size of the image
        """
        try:
            img: Image.Image = Image.open(img_path, mode='r')
        except Exception:
            raise OSError('Unable to open file')

        outputFile_name = os.path.join(
            self.output_dir, f'meme_{random.randint(0,100000000)}.png')

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        message = (str(body) + " - " + str(author))

        if message is not None:
            draw = ImageDraw.Draw(img)

            ttfFile = os.path.join(
                    os.path.dirname(__file__),
                    'fonts/LilitaOne-Regular.ttf'
                )

            try:
                font = ImageFont.truetype(ttfFile, size=30)
            except Exception:
                raise OSError('Invalid font path')

            message = textwrap.fill(text=message, width=20)

            draw.text(((random.randint(20, 250)),
                      (random.randint(20, 250))), message,
                      font=font, fill='white')

        img.save(outputFile_name)

        return os.path.relpath(path=outputFile_name, start=os.curdir)
