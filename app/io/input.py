import pandas as pd


def read_from_console():
    """
    Reads text input from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")


def read_from_file(filename):
    """
    Reads the content of a text file using built-in Python functionality.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The content of the file as a string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def read_from_pandas(filename):
    """
    Reads data from a file using the pandas library.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The text read from the file.
    """
    return str(pd.read_csv(filename))
