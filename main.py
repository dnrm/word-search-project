import os
from word_list import words
from utils import (
    fits_horizontally,
    fits_vertically,
    random_coordinate,
    random_word,
    fill_board_with_words,
    fill_remainig_spaces,
    print_board,
)


def main():
    os.system("cls||clear")
    print("===== WORD SEARCH =====")

    board_size = int(input("Enter the size of the board (default: 5): "))

    while board_size < 5:
        os.system("cls||clear")
        print("===== WORD SEARCH =====")
        print("Board size must be at least 5")
        board_size = int(input("Enter the size of the board (default: 5): "))

    board = [["" for _ in range(board_size)] for _ in range(board_size)]
    board, words_in_board = fill_board_with_words(board, words)
    board = fill_remainig_spaces(board)

    os.system("cls||clear")
    print("===== WORD SEARCH =====")
    print_board(board)

    for i in words_in_board:
        print(f"{i['word']} is at {i['coord']} in direction {i['direction']}")


if __name__ == "__main__":
    main()
