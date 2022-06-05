"""QuoteModel model for body and author text encapsulation."""


class QuoteModel:
    """QuoteModel class with body and author parameters.

    Args:
        body (str): Quote which forms the body.
        author (str): Name of author of the quote.
    Returns:
        QuoteModel: Object with body and author.
    """

    def __init__(self, body: str, author: str):
        """Initiate string parameters body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of an object string."""
        return f"Body: {self.body} - Author: {self.author}"

    def __str__(self):
        """Print out class representation as a string."""
        return f"Body: {self.body} - Author: {self.author}"
