import os
from word_list import words
from utils import (
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

    # Prints words, their position, and direction.
    # for i in words_in_board:
    #     print(f"{i['word']} is at {i['coord']} in direction {i['direction']}")

    # * Next steps are to allow user to input the coordinates of the word they've found and check if it's correct and in the words_in_board list
    # * If it is, then the word will be marked as found and the board will be printed again
    # * If all words are found, then the game will end

    # ? Possible additions: Include a timer with a cloud-based leaderboard to track the fastest times


if __name__ == "__main__":
    main()
