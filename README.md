### MEME GENERATOR  ###
Program generates a meme using an image and an overlaying quote.

#### Overview
Meme generator is a python 3.9x project.<br />
Run Meme from an argparse command-line interface (CLI) or as a Flask web-app.

#### Set-up and Run Instructions
1. Clone Meme generator project from github.
2. Install and activate virtual environment:<br />
    ~meme $source env/Scripts/activate
3. Install requirements in the shell.
4. Run program from main.py using the CLI interface:<br />
    ~meme/src $python main.py
5. Alternatively, run program as a Flask web app:<br />
    ~/meme/src $python app.py<br />
    Then in web browser: http://127.0.0.1:5000

#### Key Modules
QuoteEngine Module<br />
    Uses Interface and Ingestor Interface abstract base and generic classes<br />
    to parse quotes from CSVIngest, DocxIngest, PDFIngest and TxtIngest files.

MemeEngine Module<br />
    Used to select a random image and write a quote parsed from the QuoteEngine<br />
    Module to create a meme.

QuoteModel<br />
    Model for body and author text encapsulation.

#### Dependencies
Install the project dependencies with:
$ pip install -r requirements.txt

#### CLI Examples
Test 1: No parameter values are given<br />
Expected: Meme generated with random image and quote<br />
~/meme/src $python main.py

Test 2: All valid parameter values are given (path, body, author)<br />
Expected: Meme generated with image and text<br />
~/meme/src $python main.py --path './_data/photos/dog/xander_1.jpg'<br />
body-- 'This is a test' author-- 'Teacher"<br />

Test 3:  Only valid path parameter is given<br />
Expected: Meme generated with image in path given<br />
~/meme/src $python main.py --path './_data/photos/dog/xander_1.jpg'

Test 4: Only invalid path parameter is given<br />
Expected:  Exception stating unable to open image<br />
~/meme/src $python main.py --path './_data/photos/dog/noimage_.jpg'

Test 5: Only valid body is given<br />
Expected: Exception stating author is required if body is given <br />
~/meme/src $python main.py --body 'This is a test'

Test 6: Only valid author is given <br />
Expected: Defaults to random selection of quote author and body<br />
~/meme/src $python main.py --author 'Teacher'

#### Flask App Examples
Web interface using flask and requests.

Test 1: Launch Flask app<br />
Expected: Get random meme image and generate random quote

Test 2: Pn Flask web app select "Random" button:<br />
Expected: Get another random meme image and generate random quote

Test 3: On Flask web app select "Creator" button:<br />
http://127.0.0.1:5000/create<br />
Expected: Create meme_form.html appears

Test 4: Flask web app "Create" form.<br />
Post input values of valid image url and text for body and author<br />
img_url: https://images.rawpixel.com/image_1300/ \<br /> cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L2ZsNDgyNDQxMTEwOS1pbWFnZ \<br />
S1rcHFrNXh0eC5qcGc.jpg
body:   Meow, meow <br />
Author: Kitty <br />
Expected: Meme created with image and text in ./static

Test 5: Flask web app Create form.<br />
Post input vlaues of invalid image url and no text for body, author<br />
Expected: Validation of each form field will display
