import os
import re


class Analyze:
    """
    This class represents a text analyzer.
    """
    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise Exception('File does not exists')
        self.file_name = file_name
        self.file = Analyze.__read_file(file_name)
        pass

    @staticmethod
    def __read_file(file_name):
        with open(file_name, "r") as my_file:
            return my_file.read()

    def char_count(self):
        number_of_characters = len(self.file)
        return number_of_characters

    def word_count(self):
        words = re.findall(r'\w+', self.file.lower())
        return len(words)

    def sentence_count(self):
        sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', self.file)
        sentences = sentences[:-1]
        sentence_count = len(sentences)
        return sentence_count


def main():
    file = "Text.txt"
    try:
        text = Analyze(file)
        print('Number of characters:', text.char_count())
        print('Number of words:', text.word_count())
        print('Number of sentences:', text.sentence_count())
    except OSError as e:
        print(e)


main()
