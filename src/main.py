"""CLI interface to generate meme method using argparse."""
import argparse
from MemeEngine import MemeEngine
from meme import generate_meme
import sys

args = None
parser = argparse.ArgumentParser(description='Parse Meme CLI arguments.')
parser.add_argument('--path', help='path to an image file', default=None)
parser.add_argument('--body', help='body added to image', dest='body',
                    type=lambda x: x if x.isalpha() and len(x) <= 60 else
                    sys.exit(1), default=None)

parser.add_argument('--author', help='author added to image', dest='author',
                    type=lambda x: x if x.isalpha() and len(x) <= 60 else
                    sys.exit(1), default=None)

args = parser.parse_args()

print("Created meme: ", generate_meme(args.path, args.body, args.author))
