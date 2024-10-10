import random


def print_board(board):
    print("  ", end=" ")
    for i in range(len(board)):
        print(i, end="  ")
    print()
    index = 0
    for i in board:
        print(index, end="  ")
        for j in i:
            print(j, end="  ")
        print()
        index += 1


def fits_horizontally(board, word, coord):
    if coord[1] + len(word) <= len(board):
        for j in range(len(word)):
            if board[coord[0]][coord[1] + j] != "":
                return False
        return True
    return False


def fits_vertically(board, word, coord):
    if coord[0] + len(word) <= len(board):
        for j in range(len(word)):
            if board[coord[0] + j][coord[1]] != "":
                return False
        return True
    return False


def random_coordinate(dimensions):
    return (random.randint(0, dimensions - 1), random.randint(0, dimensions - 1))


def random_word(words):
    return words[random.randint(0, len(words) - 1)]


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
        if direction == 0:
            if fits_horizontally(board, word, coord):
                words_in_board.append(
                    {"coord": coord, "word": word, "direction": direction}
                )
                for j in range(len(word)):
                    board[coord[0]][coord[1] + j] = word[j]
        elif direction == 1:
            if fits_vertically(board, word, coord):
                words_in_board.append(
                    {"coord": coord, "word": word, "direction": direction}
                )
                for j in range(len(word)):
                    board[coord[0] + j][coord[1]] = word[j]
        else:
            print("Word does not fit in the board")
            continue

    print(words_in_board)
    return board, words_in_board


def fill_remainig_spaces(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                # * Fill with lowercase letters
                board[i][j] = chr(random.randint(97, 122))
    return board
