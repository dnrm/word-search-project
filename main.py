# Written by Daniel Medina
# Date: 2024-10-11

# ? Possible additions: Include a GUI for the game

import os
import word_list
from utils import (
    fill_board_with_words,
    fill_remainig_spaces,
    print_board,
    mark_in_board,
    prompt_wordlist,
)
import time

end_color = "\033[0m"


def main():
    os.system("cls||clear")
    print("===== WORD SEARCH =====")

    board_size = int(input("Enter the size of the board (default: 5): "))

    while board_size < 5:
        os.system("cls||clear")
        print("===== WORD SEARCH =====")
        print(f"\033[91m❌ Board size must be at least 5 {end_color}")
        board_size = int(input("Enter the size of the board (default: 5): "))

    # * Prompt user to select a wordlist
    wordlist = prompt_wordlist()
    words = word_list.words[int(wordlist)]

    # * Create the board and fill it with words
    board = [["" for _ in range(board_size)] for _ in range(board_size)]
    board, words_in_board = fill_board_with_words(board, words)
    board = fill_remainig_spaces(board)

    os.system("cls||clear")
    print("===== WORD SEARCH =====")
    print_board(board)

    # Prints words, their position, and direction.
    for i in words_in_board:
        print(f"{i['word']} is at {i['coord']} in direction {i['direction']}")

    start_time = time.time()

    # * Game loop
    while not all([i["found"] for i in words_in_board]):
        os.system("cls||clear")
        print("===== WORD SEARCH =====")
        print_board(board)

        # * Display words found and not found
        print("Words found:")
        for i in words_in_board:
            if not i["found"]:
                print(f"\033[91m{i['word']}{end_color}")
            else:
                print(f"\033[92m{i['word']}{end_color}")

        guess = input("Enter the word you found: ").lower()
        coords = input(
            "Enter the position of the first letter (example: 1,2): "
        ).lower()

        # TODO Missing to validate that coords are the correct value
        coords = coords.split(",")
        print("coords", coords)

        while guess not in words:
            print(f"\033[91m❌ Try again.{end_color}")
            guess = input("Enter the word you found: ").lower()

        for i in words_in_board:
            if i["word"] == guess:
                if coords[0] == str(i["coord"][0]) and coords[1] == str(i["coord"][1]):
                    print(f"\033[92m✅ {guess} found at {i['coord']}\033[0m")
                    time.sleep(0.75)
                    mark_in_board(i["word"], i["coord"], i["direction"], board)
                    i["found"] = True
                    break
                else:
                    print(
                        f"\033[91m❌ {guess} is not at {coords}. Try again.{end_color}"
                    )
                    time.sleep(0.75)
                    break

    os.system("cls||clear")
    print("===== WORD SEARCH =====")
    print_board(board)

    time_taken = time.time() - start_time

    print("\033[92m🎉🎉🎉 Congratulations! You found all the words! 🎉🎉🎉\033[0m")
    print(
        "You took \033[96m{:.2f}\033[0m seconds to complete the game".format(
            time_taken
        )
    )

    file = open('results.txt', 'a+')
    scores = []

    # read all lines
    for line in file:
        scores.append(line)

    # add new score
    scores.append("{:.2f}".format(time.time() - start_time))

    # sort scores
    scores.sort()

    if scores[0] == "{:.2f}".format(time.time() - start_time):
        print("\033[92m🎉🎉🎉 New high score! 🎉🎉🎉\033[0m")

    for score in scores:
        file.write(score + "\n")
    file.close()

if __name__ == "__main__":
    main()
