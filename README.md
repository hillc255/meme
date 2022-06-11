### Meme Generator
Program generates a meme with an image and an overlaying quote.

#### Overview
Meme generator utilizes an argparse command-line interface (CLI) and Flask web-app tool.

#### Set-up and Run Instructions


#### Modules & Sub-modules Roles and Responsibilities
QuoteEngine Module
   Uses Ingestor Interface abstract base and generic classes to ingest and parse quotes from CSVIngest, DocxIngest, PDFIngest and TxtIngest files.

MemeEngine Module
   Used to select a random image and write a quote selected from the QuoteEngine Module on it to create a meme.

#### Dependencies
Ingestor
QuoteModel provides model for the quote body and quote author.

#### Examples of Use