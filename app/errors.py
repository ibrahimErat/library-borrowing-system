class LibraryError(Exception):
    """A business rule was broken.

    Domain functions raise it with a message a user can read, for example
    LibraryError("No copies of this book are available."). Routes catch it
    and show the message with flash().
    """
