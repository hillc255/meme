"""Meme generator module with generate_meme method."""
import os
import random
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate meme method given a path, quote body and quote author."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []

        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
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

        quote = random.choice(quotes)

    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine.MemeEngine('./tmp')

    path = meme.make_meme(img, quote.body, quote.author, width=500)

    return path


if __name__ == "__main__":
    args = None
    parser = argparse.ArgumentParser(description='Parse Meme CLI arguments.')
    parser.add_argument('--path', help='path to an image file', default=None)
    parser.add_argument('--body', help='quote body to add to the image',
                        default=None)
    parser.add_argument('--author', help='quote author to add to the image',
                        default=None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
