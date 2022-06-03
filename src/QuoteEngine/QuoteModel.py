
class QuoteModel:
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        return f"Body: {self.body} - Author: {self.author}"

    def __str__(self):
        return f"Body: {self.body} - Author: {self.author}"


#Implement basic object-oriented data structures.
#The code includes a Python class that defines a QuoteMode object, which 
# contains text fields for body and author. The class overrides the correct 
# methods to instantiate the class and print the model contents as: 
# ”body text” - author
#All related classes are defined in a directory that includes
#  valid __init__.py files to declare the package.

