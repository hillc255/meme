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

#### Examples of Use