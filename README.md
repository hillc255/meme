### MEME GENERATOR
Program generates a meme with an image and an overlaying quote.

#### Overview
Meme generator utilizes an argparse command-line interface (CLI) and Flask web-app tool.

#### Set-up and Run Instructions


#### Modules & Sub-modules Roles and Responsibilities
QuoteEngine Module
    Uses Interface and Ingestor Interface abstract base and generic classes
    to parse quotes from CSVIngest, DocxIngest, PDFIngest and TxtIngest files.

MemeEngine Module
    Used to select a random image and write a quote parsed from the 
    QuoteEngine Module to create a meme.

#### Dependencies
QuoteModel
    Provides a model for the quote body and quote author.

#### CLI Examples
Test 1: No parameter values are given
Expected: Meme generated with random image and quote
$python src/main.py

Test 2: All valid parameter values are given (path, body, author)
Expected: Meme generated with image and text
$python src/main.py --path './_data/photos/dog/xander_1.jpg' body-- 'This is a test' author-- 'Teacher"

Test 3:  Only valid path parameter is given
Expected: Meme generated with image in path given
$python src/main.py --path './_data/photos/dog/xander_1.jpg'

Test 4: Only invalid path parameter is given
Expected:  Exception stating unable to open image
$python src/main.py --path './_data/photos/dog/noimage_.jpg'

Test 5: Only valid author or valid body is given
Expected: Exception stating both author and body values must be given 
$python src/main.py --author 'Teacher'
or
$python src/main.py --body 'This is a test'