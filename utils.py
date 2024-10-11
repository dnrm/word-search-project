import random
end_color = '\033[0m'

def random_color():
    return f"\033[{random.randint(101, 105)}m"

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


def fill_remainig_spaces(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                # * Fill with lowercase letters
                board[i][j] = chr(random.randint(97, 122))
    return board

def mark_in_board(word, coordinate, direction, board):
    color = random_color()
    if direction == 0:
        for i in range(len(word)):
            board[coordinate[0]][coordinate[1] + i] = f"{color}{board[coordinate[0]][coordinate[1] + i].upper()}{end_color}"
    else:
        for i in range(len(word)):
            board[coordinate[0] + i][coordinate[1]] = f"{color}{board[coordinate[0] + i][coordinate[1]].upper()}{end_color}"
    return board