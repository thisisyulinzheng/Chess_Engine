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
                chessboard[row].append(position[count])
            else:
                for i in range(0, int(position[count])):
                    chessboard[row].append('+')
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
            if (chessboard[i][j] != '+'):
                s+=("| {}  ".format(translate_piece(chessboard[i][j])))
            else:
                s+=("|    ")
        s+=("|")
        print(s)
    print("-------------------------------------------")


def translate_piece(p):
    if (p == 'P'):
        return '♙'
    if (p == 'N'):
        return '♘'
    if (p == 'B'):
        return '♗'
    if (p == 'R'):
        return '♖'
    if (p == 'Q'):
        return '♕'
    if (p == 'K'):
        return '♔'
    if (p == 'p'):
        return '♟'
    if (p == 'n'):
        return '♞'
    if (p == 'b'):
        return '♝'
    if (p == 'r'):
        return '♜'
    if (p == 'q'):
        return '♛'
    if (p == 'k'):
        return '♚'
