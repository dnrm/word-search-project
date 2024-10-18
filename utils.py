import random

end_color = "\033[0m"

"""
@random_color_highlight
Returns a random color code for highlighting text
"""


def random_color_highlight():
    return f"\033[{random.randint(101, 105)}m"


"""
@random_color
Returns a random color code for text
"""


def random_color():
    return f"\033[{random.randint(91, 96)}m"


"""
@prompt_wordlist
Prompts the user to select a wordlist and returns the selection
It has validation so that the user can only select a number between 1 and 6
"""


def prompt_wordlist():
    print("Which wordlilst would you like to use?")
    print(f"\033[92m1. Fruit{end_color}")
    print(f"\033[92m2. Programming Languages{end_color}")
    print(f"\033[92m3. Animals{end_color}")
    print(f"\033[92m4. Tec de Monterrey Edition{end_color}")
    print(f"\033[92m5. Cities Around the World{end_color}")
    print(f"\033[92m6. Car Brands{end_color}")

    wordlist_selection = 0
    wordlist_selection = input(
        "Enter the number of the wordlist you would like to use (default 1): "
    )

    while wordlist_selection < "1" or wordlist_selection > "6":
        print(f"\033[91m❌ Invalid option{end_color}")
        wordlist_selection = input(
            "Enter the number of the wordlist you would like to use (default 1): "
        )

    return wordlist_selection


"""
@print_board
Prints the board with the corresponding indexes and in a nice format.
"""


def print_board(board):
    print("  ", end=" ")
    for i in range(len(board)):
        print(f"\033[36m{i}{end_color}", end="  ")
    print()
    index = 0
    for i in board:
        print(f"\033[36m{index}{end_color}", end="  ")
        for j in i:
            print(j, end="  ")
        print()
        index += 1


"""
@fits_horizontally
Checks if a word fits horizontally in the board by checking if the word is
not longer than the board and if the spaces are empty.
"""


def fits_horizontally(board, word, coord):
    if coord[1] + len(word) <= len(board):
        for j in range(len(word)):
            if board[coord[0]][coord[1] + j] != "":
                return False
        return True
    return False


"""
@fits_vertically
Checks if a word fits vertically in the board by checking if the word is
not longer than the board and if the spaces are empty.
"""


def fits_vertically(board, word, coord):
    if coord[0] + len(word) <= len(board):
        for j in range(len(word)):
            if board[coord[0] + j][coord[1]] != "":
                return False
        return True
    return False


"""
@random_coordinate
Returns a random coordinate based on the dimensions of the board
"""


def random_coordinate(dimensions):
    return (random.randint(0, dimensions - 1), random.randint(0, dimensions - 1))


"""
@random_word
Returns a random word from the list of words
"""


def random_word(words):
    return words[random.randint(0, len(words) - 1)]


"""
@fill_board_with_words
Fills the board with words from the list of words by selecting a random word,
checking if it fits in the board, and then placing it in the board.

The direction is randomly assigned, 0 for horizontal and 1 for vertical.
"""


def fill_board_with_words(board, words):
    # * Filter out words that are longer than the board
    valid_words = []
    words_in_board = []

    for i in words:
        if len(i) > len(board):
            continue
        valid_words.append(i)

    for i in range(len(valid_words) * 2):
        coord = random_coordinate(len(board))
        word = random_word(valid_words)

        direction = random.randint(0, 1)

        # * 0: Horizontal | 1: Vertical
        if direction == 0 and word not in [i["word"] for i in words_in_board]:
            if fits_horizontally(board, word, coord):
                words_in_board.append(
                    {
                        "coord": coord,
                        "word": word,
                        "direction": direction,
                        "found": False,
                    }
                )
                for j in range(len(word)):
                    board[coord[0]][coord[1] + j] = word[j]
        elif direction == 1 and word not in [i["word"] for i in words_in_board]:
            if fits_vertically(board, word, coord):
                words_in_board.append(
                    {
                        "coord": coord,
                        "word": word,
                        "direction": direction,
                        "found": False,
                    }
                )
                for j in range(len(word)):
                    board[coord[0] + j][coord[1]] = word[j]
        else:
            print("Word does not fit in the board")
            continue

    return board, words_in_board


"""
@fill_remaining_spaces
Fills the remaining spaces in the board with random lowercase letters by
checking if the space is empty.
"""


def fill_remainig_spaces(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                # * Fill with lowercase letters
                board[i][j] = chr(random.randint(97, 122))
    return board


"""
@mark_in_board
Marks the word in the board with a random color by checking the direction
and then highlighting the word in the board by appending the color codes
necessary.
"""


def mark_in_board(word, coordinate, direction, board):
    color = random_color_highlight()
    if direction == 0:
        for i in range(len(word)):
            board[coordinate[0]][
                coordinate[1] + i
            ] = f"{color}{board[coordinate[0]][coordinate[1] + i].upper()}{end_color}"
            print(f"{coordinate[0]} {coordinate[1] + i}")
    else:
        for i in range(len(word)):
            board[coordinate[0] + i][
                coordinate[1]
            ] = f"{color}{board[coordinate[0] + i][coordinate[1]].upper()}{end_color}"
    return board
