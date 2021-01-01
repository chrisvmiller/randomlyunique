Date: 2020-11-12
Title: Scrabble Art Generator
Category: random
Slug: scrabble-art-generator
Summary: Nothing says respectable bourgeoisie home decor more than a used Scrabble board nailed to your wall.

I completely believe that displaying a purchased canvas of "A Starry Night" - although beautiful - totally misses the inherit personal nature of art. With this in mind, I acquired a used copy of Scrabble for some board game themed wall art! My goal: scrabbly connecting a bunch of adjectives to my name. 

Instead of manually finding a hodgepodge of properly connected adjectives, I decided to automate this search. In a nutshell, this super naive algorithm boils down to a 2 dimensional regex solver that randomly samples adjectives from Wordnet.


![Photo]({attach}/assets/random/2020/scrabble-art-generator.png){.image_center_style}

    :::python
    import argparse
    import random
    import re
    import numpy as np
    from nltk.corpus import wordnet as wn


    class Scrabbler():
        def __init__(self, my_name, board_size):
            self.name = my_name
            self.board_size = board_size

            self.board = np.empty([board_size, board_size], dtype=object)
            self.board[:] = r'.?'

            self.used_words = []
            self.look_at_rows = False

            self.read_clean_word_list()
            self.place_name_on_board()

        def read_clean_word_list(self):
            all_words = set()
            for adjective in wn.all_synsets(wn.ADJ):
                # Remove Roman Numerals
                if 'more than' in adjective.definition():
                    continue
                for lemma in adjective.lemma_names():
                    if lemma.isalpha() and len(lemma) < self.board_size:
                        all_words.add(lemma.lower())

            self.all_words = list(all_words) + [self.name]

        def place_name_on_board(self):
            starting_loc = (self.board_size - len(self.name)) // 2
            end_loc = starting_loc + len(self.name)
            center_row = self.board_size // 2
            self.board[center_row][starting_loc:end_loc] = list(self.name)

        @staticmethod
        def try_to_place(line, word):
            if any(characters.isalpha() for characters in line):
                smushed_line = f'^{"".join(line)}$'
                smushed_line_regrex = re.compile(smushed_line)

                if smushed_line_regrex.search(word):
                    num_characters_in_line = sum(
                        characters.isalpha() for characters in line
                    )
                    word_length = len(word)

                    for position in range(0, len(line) - word_length):
                        new_line = [' '] * len(line)
                        new_line[position:position+word_length] = list(word)

                        total_in_common = sum(
                            1 if a == b else 0 for (a, b) in zip(line, new_line)
                        )

                        if total_in_common == num_characters_in_line:
                            revert_back_to_regex = [
                                '.?' if c == ' ' else c for c in new_line
                            ]
                            return revert_back_to_regex

        def placeWord(self, board, word):
            self.temp_board = None
            copied_board = np.copy(board)

            for index, line in enumerate(board):
                letters_in_common = set(line).intersection(set(word))
                if len(letters_in_common) > 0:
                    new_word = self.try_to_place(line, word)
                    if new_word:
                        copied_board[index] = new_word
                        self.temp_board = copied_board
                        break

        def check_for_valid_lines(self):
            if self.temp_board is None:
                return False

            for temp_board_orientation in [self.temp_board, self.temp_board.T]:
                for row in temp_board_orientation:
                    words = row.sum().replace('.?', ' ').split()
                    for word in words:
                        if len(word) > 1:
                            if not word in self.all_words:
                                return False

            return True

        def add_valid_word_to_board(self):
            random.shuffle(self.all_words)

            for word in self.all_words:
                if word in self.used_words:
                    continue

                if self.look_at_rows:
                    self.placeWord(self.board, word)
                else:
                    self.placeWord(self.board.T, word)

                is_valid = self.check_for_valid_lines()
                if is_valid:
                    if not self.look_at_rows:
                        self.temp_board = self.temp_board.T
                    self.board[:, :] = self.temp_board
                    return word

        def print_board(self):
            print('\n')
            for row in self.board:
                clean_row = "".join(row).replace(".?", " ")
                print(clean_row)

        def run(self):
            while True:
                valid_word = self.add_valid_word_to_board()
                print('.', end="", flush=True)
                if not valid_word:
                    break

                self.look_at_rows = ~self.look_at_rows
                self.used_words.append(valid_word)

            self.print_board()


    def check_wordnet_exists():
        try:
            wn.fileids()
        except LookupError:
            print('Downloading wordnet, is this okay? (y/n)')
            if input() == 'y':
                import nltk
                nltk.download('wordnet')
            else:
                exit()


    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', nargs='*', help='Sets your name')
        parser.add_argument('--size', type=int, default=15,
                            help='Sets the size of the board')
        parser.add_argument('--iter', type=int, default=1,
                            help='Sets the number of boards generated')
        args = parser.parse_args()

        my_name = "".join(args.name).lower()
        board_size = args.size
        number_of_iterations = args.iter

        if not my_name:
            print("Missing `--name <My Name>` argument")
            exit()
        elif len(my_name) > board_size:
            board_size = len(my_name)

        check_wordnet_exists()

        print('Running Scrabbler\n')
        for _ in range(number_of_iterations):
            scrabbler = Scrabbler(my_name, board_size)
            scrabbler.run()


<p align="center">
    <a class="nounderline" href="{attach}/assets/random/2020/scrabbler.py">Download</a>
</p>
