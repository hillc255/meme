import os
import random
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel
import argparse


# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        #get desired image path with os.walk
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        #select random image path
        img = random.choice(imgs)
        print(f"\nimg: ", img)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        #select random quote with author
        quote = random.choice(quotes)
        print(f"quote: ", quote)

    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    #constructed MemeEngine with output directory
    meme = MemeEngine('./tmp')

    print("After meme constructor")

    #making the meme
    path = meme.make_meme(img, quote.body, quote.author, width=500) 

    print(f"path: ", path)

    #constructed meme full path
    return path


if __name__ == "__main__":
    args = None  #why is this needed?
    parser = argparse.ArgumentParser(description='Parse Meme CLI arguments.')
    parser.add_argument('--path', help='path to an image file', default=None)
    parser.add_argument('--body', help='quote body to add to the image', default=None)
    parser.add_argument('--author', help='quote author to add to the image', default=None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
#$ python meme.py

#IMG:  ./_data/photos/dog/xander_2.jpg

#QUOTE:  Life is like peanut butter: crunchy - Peanut
#None
