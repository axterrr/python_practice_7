import pandas as pd


def write_to_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): The text to be printed.

    returns:
        None
    """
    print(text)
    return None


def write_to_file(filename, text):
    """
    Writes text to a file using built-in Python functionality.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written.

    returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return None


def write_to_pandas(filename, text):
    """
    Writes text to a file using the pandas library.

    Args:
        filename (str): The name of the file to save the data to.
        text (str): The text to be written to the file.

    returns:
        None
    """
    df = pd.DataFrame({'data': [text]})
    df.to_csv(filename, index=False)
    return None
