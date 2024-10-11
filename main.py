import os
from word_list import words
from utils import (
    fill_board_with_words,
    fill_remainig_spaces,
    print_board,
)
import time

end_color = '\033[0m'

def main():
    os.system("cls||clear")
    print("===== WORD SEARCH =====")

    board_size = int(input("Enter the size of the board (default: 5): "))

    while board_size < 5:
        os.system("cls||clear")
        print("===== WORD SEARCH =====")
        print(f"\033[91m❌ Board size must be at least 5 {end_color}")
        board_size = int(input("Enter the size of the board (default: 5): "))

    board = [["" for _ in range(board_size)] for _ in range(board_size)]
    board, words_in_board = fill_board_with_words(board, words)
    board = fill_remainig_spaces(board)

    os.system("cls||clear")
    print("===== WORD SEARCH =====")
    print_board(board)

    # Prints words, their position, and direction.
    for i in words_in_board:
        print(f"{i['word']} is at {i['coord']} in direction {i['direction']}")

    # * Next steps are to allow user to input the coordinates of the word they've found and check if it's correct and in the words_in_board list
    # * If it is, then the word will be marked as found and the board will be printed again
    # * If all words are found, then the game will end

    # ? Possible additions: Include a timer with a cloud-based leaderboard to track the fastest times
    # ? Possible additions: Include a GUI for the game


    while not all([i["found"] for i in words_in_board]):
        os.system("cls||clear")
        print("===== WORD SEARCH =====")
        print_board(board)
        for i in words_in_board:
            if not i["found"]:
                # print(f"\033[92m{i['word']} is at {i['coord']} in direction {i['direction']}{end_color}")
                print(f"\033[91m{i['word']}{end_color}")
            else:
                print(f"\033[92m{i['word']}{end_color}")

        guess = input("Enter the word you found: ").lower()
        while guess not in words:
            guess = input("Enter the word you found: ").lower()

        for i in words_in_board:
            if i["word"] == guess:
                print(f"\033[92m✅ {guess} found at {i['coord']} in direction {i['direction']} \033[0m")
                time.sleep(1.2)
                i["found"] = True
                break
        
    os.system("cls||clear")
    print("===== WORD SEARCH =====")
    print_board(board)

    print("\033[92m🎉🎉🎉 Congratulations! You found all the words! 🎉🎉🎉\033[0m")


if __name__ == "__main__":
    main()
