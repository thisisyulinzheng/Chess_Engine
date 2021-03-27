def setup_board(position):
    chessboard = []
    for i in range(0, 8):
        chessboard.append([])
    fen_pos = len(position)
    count = 0
    row = 0
    col = 0
    while (count < fen_pos):
        if (position[count] == '/'):
            row += 1
        else:
            if (position[count] > '9'):
                chessboard[row].append(letter_to_num(position[count]))
            else:
                for i in range(0, int(position[count])):
                    chessboard[row].append(0)
        count += 1
    return chessboard;

def print_board(chessboard):
    print("  | a  | b  | c  | d  | e  | f  | g  | h  |")
    s = ''
    for i in reversed(range(8)):
        print("-------------------------------------------")
        s = ''
        s+=("{} ".format(i + 1))
        for j in reversed(range(8)):
            if (chessboard[i][j] != 0):
                s+=("| {}  ".format(piece_to_symbol(chessboard[i][j])))
            else:
                s+=("|    ")
        s+=("|")
        print(s)
    print("-------------------------------------------")

def letter_to_num(p):
    if (p == 'P'):
        return 4
    if (p == 'N'):
        return 12
    if (p == 'B'):
        return 13
    if (p == 'R'):
        return 20
    if (p == 'Q'):
        return 36
    if (p == 'K'):
        return 100000
    if (p == 'p'):
        return -4
    if (p == 'n'):
        return -12
    if (p == 'b'):
        return -13
    if (p == 'r'):
        return -20
    if (p == 'q'):
        return -36
    if (p == 'k'):
        return -100000

def num_to_letter(p):
    if (p == 4):
        return 'P'
    if (p == 12):
        return 'N'
    if (p == 13):
        return 'B'
    if (p == 20):
        return 'R'
    if (p == 36):
        return 'Q'
    if (p == 100000):
        return 'K'
    if (p == -4):
        return 'p'
    if (p == -12):
        return 'n'
    if (p == -13):
        return 'b'
    if (p == -20):
        return 'r'
    if (p == -36):
        return 'q'
    if (p == -100000):
        return 'k'

def piece_to_symbol(p):
    if (p == 4):
        return '♙'
    if (p == 12):
        return '♘'
    if (p == 13):
        return '♗'
    if (p == 20):
        return '♖'
    if (p == 36):
        return '♕'
    if (p == 100000):
        return '♔'
    if (p == -4):
        return '♟'
    if (p == -12):
        return '♞'
    if (p == -13):
        return '♝'
    if (p == -20):
        return '♜'
    if (p == -36):
        return '♛'
    if (p == -100000):
        return '♚'
