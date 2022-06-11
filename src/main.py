"""CLI interface to generate_meme method using argparse."""
import argparse
from MemeEngine import MemeEngine
from meme import generate_meme

args = None
parser = argparse.ArgumentParser(description='Parse Meme CLI arguments.')
parser.add_argument('--path', help='path to an image file', default=None)
parser.add_argument('--body', help='quote body to add to the image',
                    default=None)
parser.add_argument('--author', help='quote author to add to the image',
                    default=None)
args = parser.parse_args()

print("Created meme: ", generate_meme(args.path, args.body, args.author))

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
#$ python main.py --path './_data/photos/dog/xander_1.jpg'
