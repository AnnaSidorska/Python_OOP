class Analyze:
    def __init__(self, name_of_file):
        self.__name = name_of_file

    def print_file(self):
        with open(self.__name) as my_file:
            for line in my_file:
                print(line)

    def char_count(self):
        with open(self.__name) as my_file:
            data = my_file.read()
            number_of_characters = len(data)
            return number_of_characters

    def word_count(self):
        with open(self.__name) as my_file:
            data = my_file.read()
            words_list = data.split()
            return len(words_list)

    def sentence_count(self):
        with open(self.__name) as my_file:
            data = my_file.read()
            number_of_stops = data.count('.') + data.count('?') + data.count('!') + data.count('...') + data.count('!?')
            return number_of_stops

    def space_count(self):
        with open(self.__name) as my_file:
            data = my_file.read()
            number_of_spaces = data.count(" ")
            return number_of_spaces


def main():
    text = Analyze("C://Text.txt")
    text.print_file()
    print('Number of characters: ', text.char_count())
    print('Number of words: ', text.word_count())
    print('Number of sentences: ', text.sentence_count())
    print('Number of whitespaces: ', text.space_count())


main()
