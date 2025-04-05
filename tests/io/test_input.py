import unittest
from pandas.errors import EmptyDataError
from app.io.input import read_from_file, read_from_pandas


class TestInputFunctions(unittest.TestCase):

    def test_read_from_file_reads_text(self):
        file_path = '../../data/text.txt'
        expected_text = "Some very cool text."
        with open(file_path, 'w') as file:
            file.write(expected_text)
        actual_text = read_from_file(file_path)
        self.assertEqual(expected_text, actual_text)


    def test_read_from_file_not_found(self):
        file_path = '../../data/non_existing_file.txt'
        with self.assertRaises(FileNotFoundError):
            read_from_file(file_path)


    def test_read_from_file_empty(self):
        file_path = '../../data/text.txt'
        with open(file_path, 'w') as file:
            file.write("")
        result = read_from_file(file_path)
        self.assertEqual("", result)


    def test_read_from_pandas_reads_text(self):
        file_path = '../../data/text.csv'
        expected_text = "Empty DataFrame\nColumns: [Col1]\nIndex: []"
        text_to_write = "Col1"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_to_write)
        actual_text = read_from_pandas(file_path)
        print(actual_text)
        self.assertEqual(expected_text, actual_text)


    def test_read_from_pandas_not_found(self):
        file_path = '../../data/non_existing_file.csv'
        with self.assertRaises(FileNotFoundError):
            read_from_pandas(file_path)


    def test_read_from_pandas_empty(self):
        file_path = '../../data/text.csv'
        with open(file_path, 'w') as file:
            file.write("")
        with self.assertRaises(EmptyDataError):
            read_from_pandas(file_path)


if __name__ == '__main__':
    unittest.main()
