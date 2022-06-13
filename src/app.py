"""Flask app using QuoteEngine and MemeEngine modules to generate a meme."""
import random
import os
import requests
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from flask import Flask, render_template, abort, request
from PIL import Image
from io import BytesIO
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

dirname = os.path.dirname(__file__)

if not os.path.exists('./static'):
    os.makedirs('./static')

meme = MemeEngine.MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/', methods=['GET'])
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    print(f"\nappy.py img: ", img)

    quote = random.choice(quotes)
    print(f"app.py quote: {quote}")

    outputFile_name = meme.make_meme(img, quote.body, quote.author)
    print(f"app.py path:  {outputFile_name}")

    return render_template('meme.html', path=outputFile_name)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    error = None

    img_url = request.form.get('image_url')

    if img_url is None:
        error = "Invalid image URL"
        abort(404)

    response = requests.get(img_url)

    if response.status_code != 200:
        error = "Invalid image URL"
    else:
        try:
            img_response = Image.open(BytesIO(response.content))
        except HTTPException:
            error = "Invalid image URL"
            abort(500)

        if not os.path.exists("./tmp"):
            os.makedirs("./tmp")

        img_path = os.path.join("./tmp",
                                f'meme_{random.randint(0,100000000)}.png')

        img_response.save(img_path)

        body = request.form.get('body', "")
        author = request.form.get('author', "")

        path = meme.make_meme(img_path, body, author)

        os.remove(img_path)

        return render_template('meme.html', path=path)


@app.errorhandler(500)
def internal_error(error):
    """Error handling for 500 errors."""
    error = "Invalid image URL"
    return render_template("meme_form.html", error=error)


@app.errorhandler(404)
def not_found(error):
    """Error handling for 404 errors."""
    error = "Invalid image URL"
    return render_template("meme_form.html", error=error)


if __name__ == "__main__":
    app.run()
