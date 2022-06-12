### MEME GENERATOR  ###
Program generates a meme using an image and an overlaying quote.

#### Overview
Meme generator is a python 3.9 project.
Run Meme from an argparse command-line interface (CLI) or as a Flask web-app.

#### Set-up and Run Instructions
1. Clone Meme generator project from github.
2. Install and activate virtual environment:
    ~meme $source env/Scripts/activate
3. Install requirements in the shell.
4. Run program from main.py using the CLI interface:
    ~meme/src $python main.py
5. Alternatively, run program as a Flask web app:
    ~/meme/src $python app.py
    Then in web browser: http://127.0.0.1:5000

#### Key Modules
QuoteEngine Module
    Uses Interface and Ingestor Interface abstract base and generic classes
    to parse quotes from CSVIngest, DocxIngest, PDFIngest and TxtIngest files.

MemeEngine Module
    Used to select a random image and write a quote parsed from the QuoteEngine Module to create a meme.

QuoteModel
    Model for body and author text encapsulation.

#### Dependencies
Install the project dependencies with:
$ pip install -r requirements.txt

#### CLI Examples
Test 1: No parameter values are given
Expected: Meme generated with random image and quote
~/meme/src $python main.py

Test 2: All valid parameter values are given (path, body, author)
Expected: Meme generated with image and text
~/meme/src $python main.py --path './_data/photos/dog/xander_1.jpg' 
body-- 'This is a test' author-- 'Teacher"

Test 3:  Only valid path parameter is given
Expected: Meme generated with image in path given
~/meme/src $python main.py --path './_data/photos/dog/xander_1.jpg'

Test 4: Only invalid path parameter is given
Expected:  Exception stating unable to open image
~/meme/src $python main.py --path './_data/photos/dog/noimage_.jpg'

Test 5: Only valid body is given
Expected: Exception stating author is required if body is given 
~/meme/src $python main.py --body 'This is a test'

Test 6: Only valid author is given
Expected: Defaults to random selection of quote author and body
~/meme/src $python main.py --author 'Teacher'

#### Flask App Examples
Web interface using flask and requests.

Test 1: Launch Flask app
Expected: Get random meme image and generate random quote

Test 2: Pn Flask web app select "Random" button:
Expected: Get another random meme image and generate random quote

Test 3: On Flask web app select "Creator" button: 
http://127.0.0.1:5000/create
Expected: Create meme_form.html appears

Test 4: Flask web app "Create" form.
Post input values of valid image url and text for body and author
img_url: https://images.rawpixel.com/image_1300/\  cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L2ZsNDgyNDQxMTEwOS1pb\
WFnZS1rcHFrNXh0eC5qcGc.jpg
body:   Meow, meow
Author: Kitty
Expected: Meme created with image and text in ./static

Test 5: Flask web app Create form.
Post input vlaues of invalid image url and no text for body, author
Expected: Validation of each form field will display
