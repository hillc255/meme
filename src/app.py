from io import StringIO
import random
import os
import requests
from pathlib import Path
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, IngestorInterface, QuoteModel
from flask import Flask, render_template, abort, request
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# @TODO Import your Ingestor and MemeEngine classes--ok

app = Flask(__name__)

dirname = os.path.dirname(__file__)

meme = MemeEngine.MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable - ok

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory - ok

    imgs = []
    #get desired image path with os.walk
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

quotes, imgs = setup()


@app.route('/', methods=['GET'])
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array - ok

    img = random.choice(imgs)
    print(f"\nappy.py img: ", img)

    #img = "None"
    #quote = QuoteModel("None", "None")

    # 2. select a random quote from the quotes array - ok

    quote = random.choice(quotes)
    print(f"app.py quote: {quote}")

    outputFile_name = meme.make_meme(img, quote.body, quote.author)
    print(f"app.py path:  {outputFile_name}")
    
    return render_template('meme.html', path=outputFile_name)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.

    #get image url from meme_form.html
    img_url = request.form.get('image_url')
    
    #get the image from the url and write it with random name
    #  into tmp directory
    if img_url is None:
        abort(404)

   
    #try:
       # url = img_url.decode("utf-8")
    #except UnicodeEncodeError: 
       # pass
   

    response = requests.get(img_url) 
    if response.status_code != 200:
        print('Image Couldn\'t be retreived')
    else:
        #with open(img_url, 'rb') as f:
            #contents = f.read()
          
        img_response = Image.open(BytesIO(response.content)) 
        #img_response = Image.open(response.content)
 
 
    # save the image to a tmp directory
        img_path = os.path.join("./tmp", 
                f'meme_{random.randint(0,100000000)}.png')

        img_response.save(img_path)

        body = request.form.get('body', "")
        author = request.form.get('author', "")

    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
        path = meme.make_meme(img_path, body, author)

    # 3. Remove the temporary saved image.
        os.remove(img_path)
    
        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()


#Requirements

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
# source env/Scripts/activate
#$ python app.py
# in web browser: http://127.0.0.1:5000

#########
#Package your Application
#open app.py flask web server
#complete TODOs
#test call:  python3 app.py
#check work:  https://review.udacity.com/#!/rubrics/2709/view
#create requirements.txt file in project root to include all dependencies

#The project completes the Flask app starter code in app.py. 
# All @TODO tasks listed in the file have been completed.

#app.py 
# uses the Quote Engine module and Meme Generator modules to generate 
# a random captioned image.

#app.py 
# uses the requests package to fetch an image from a user submitted URL.

#The flask server runs with no errors

##############################
#mkdir test-env && cd test-env
#python -m venv env
#source env/bin/activate
#pip install pandas (or whatever)
#deactivate (stop virtual environment)
#git init
#echo 'env' > .gitignore
#pip freeze > requirements.txt
#git add requirements.txt
#commit files and push to a repro

#source env/Scripts/activate.bat
#env/Scripts/activate.bat
# source Scripts/activate
#####################################
# The project contains a main.py file that uses the ImageCaptioner, 
# DocxIngestor, PDFIngestor, and CSVIngestor methods to generate a 
# random captioned image.

#The program must be executable from the command line.
#The program takes three OPTIONAL arguments:

#A string quote body
#A string quote author
#An image path
#The program returns a path to a generated image.
#If any argument is not defined, a random selection is used.

#Interface with web resources using flask and requests.