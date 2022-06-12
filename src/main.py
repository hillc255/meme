"""CLI interface to generate meme method using argparse."""
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
