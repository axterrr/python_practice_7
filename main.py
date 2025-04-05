from app.io.input import read_from_console, read_from_file, read_from_pandas
from app.io.output import write_to_console, write_to_file


def main():
    input_text_console = read_from_console()
    input_text_file = read_from_file("data/data.txt")
    input_text_pandas = read_from_pandas("data/data.csv")

    write_to_console(input_text_console)
    write_to_console(input_text_file)
    write_to_console(input_text_pandas)

    write_to_file("data/result_from_console.txt", input_text_console)
    write_to_file("data/result_from_file.txt", input_text_file)
    write_to_file("data/result_from_pandas.txt", input_text_pandas)


if __name__ == "__main__":
    main()
