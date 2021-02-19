from graphics import *
#starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
move_list = []

def piece_color(piece):
    p = ord(piece)
    if ((p > 96) and (p < 123)):
        return 2
    else:
        if ((p > 64) and (p < 91)):
            return 1
        else:
            return 0

def add_move(r, c, clr, sq_clr):
    if (sq_clr == 0):
        temp_list = []
        temp_list.append(r)
        temp_list.append(c)
        move_list.append(temp_list)
        return False
    else:
        if (sq_clr != clr):
            temp_list = []
            temp_list.append(r)
            temp_list.append(c)
            move_list.append(temp_list)
            return True
        else:
            return True

def in_check(row, col, clr):
    return True

def rook_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    r+=1
    while (r < 8):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r+=1
    r = row
    r-=1
    while (r >= 0):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r-=1
    r = row
    c+=1
    while (c < 8):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        c+=1
    c = col
    c-=1
    while (c >= 0):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        c-=1
    m_list = move_list[:]
    move_list.clear()
    return m_list

def bishop_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    r+=1
    c+=1
    while ((r < 8) and (c < 8)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r+=1
        c+=1
    r = row
    c = col
    r+=1
    c-=1
    while((r < 8) and (c >= 0)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r+=1
        c-=1
    r = row
    c = col
    r-=1
    c+=1
    while((r >= 0) and (c < 8)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r-=1
        c+=1
    r = row
    c = col
    r-=1
    c-=1
    while((r >= 0) and (c >= 0)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(r, c, clr, sq_clr)):
            break
        r-=1
        c-=1
    m_list = move_list[:]
    move_list.clear()
    return m_list

def knight_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    if ((r + 2 < 8) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r+2][c+1])
        add_move(r + 2, c + 1, clr, sq_clr)
    if ((r + 1 < 8) and (c + 2 < 8 )):
        sq_clr = piece_color(chessboard[r+1][c+2])
        add_move(r + 1, c + 2, clr, sq_clr)
    if ((r + 2 < 8) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r+2][c-1])
        add_move(r + 2, c - 1, clr, sq_clr)
    if ((r + 1 < 8) and (c - 2 >= 0)):
        sq_clr = piece_color(chessboard[r+1][c-2])
        add_move(r + 1, c - 2, clr, sq_clr)
    if ((r - 2 >= 0) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r-2][c-1])
        add_move(r - 2, c - 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c - 2 >= 0)):
        sq_clr = piece_color(chessboard[r-1][c-2])
        add_move(r - 1, c - 2, clr, sq_clr)
    if ((r - 2 >= 0) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r-2][c+1])
        add_move(r - 2, c + 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c + 2 < 8)):
        sq_clr = piece_color(chessboard[r-1][c+2])
        add_move(r - 1, c + 2, clr, sq_clr)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def queen_moves(chessboard, row, col):
    b_list = bishop_moves(chessboard, row, col)
    r_list = rook_moves(chessboard, row, col)
    return(b_list + r_list)

def pawn_add_move(r, c):
    temp_list = []
    temp_list.append(r)
    temp_list.append(c)
    move_list.append(temp_list)

def pawn_moves(chessboard, row, col):
    color = piece_color(chessboard[row][col])
    r = row
    c = col
    if (color == 1):
        if ((r + 1 < 8) and (c + 1 < 8)):
            p = piece_color(chessboard[r + 1][c + 1])
            if ((p != color) and (p != 0)):
                pawn_add_move(r + 1, c + 1)
        if ((r + 1 < 8) and (c - 1 >= 0)):
            p = piece_color(chessboard[r + 1][c - 1])
            if ((p != color) and (p != 0)):
                pawn_add_move(r + 1, c - 1)
        if (r + 1 < 8):
            p = piece_color(chessboard[r + 1][c])
            if (p == 0):
                pawn_add_move(r + 1, c)
                if (row == 1):
                    p1 = piece_color(chessboard[r + 2][c])
                    if (p1 == 0):
                        pawn_add_move(r + 2, c)
    else:
        if ((r - 1 >= 0) and (c + 1 < 8)):
            p = piece_color(chessboard[r - 1][c + 1])
            if ((p != color) and (p != 0)):
                pawn_add_move(r - 1, c + 1)
        if ((r - 1 >= 0) and (c - 1 >= 0)):
            p = piece_color(chessboard[r - 1][c - 1])
            if ((p != color) and (p != 0)):
                pawn_add_move(r - 1, c - 1)
        if (r - 1 >= 0):
            p = piece_color(chessboard[r - 1][c])
            if (p == 0):
                pawn_add_move(r - 1, c)
                if (row == 6):
                    p1 = piece_color(chessboard[r - 2][c])
                    if (p1 == 0):
                        pawn_add_move(r - 2, c)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def king_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    if ((r + 1 < 8) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r+1][c+1])
        add_move(r + 1, c + 1, clr, sq_clr)
    if ((r + 1 < 8) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r+1][c-1])
        add_move(r + 1, c - 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r-1][c+1])
        add_move(r - 1, c + 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r-1][c-1])
        add_move(r - 1, c - 1, clr, sq_clr)
    if (r + 1 < 8):
        sq_clr = piece_color(chessboard[r+1][c])
        add_move(r + 1, c , clr, sq_clr)
    if (r - 1 >= 0):
        sq_clr = piece_color(chessboard[r-1][c])
        add_move(r - 1, c , clr, sq_clr)
    if (c + 1 < 8):
        sq_clr = piece_color(chessboard[r][c+1])
        add_move(r , c + 1, clr, sq_clr)
    if (c - 1 >= 0):
        sq_clr = piece_color(chessboard[r][c-1])
        add_move(r , c - 1, clr, sq_clr)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def total_value(chessboard):
    val = 0
    for r in range(0,8):
        for c in range(0,8):
            p = chessboard[r][c]
            clr = piece_color(p)
            if (p != '+'):
                if (clr == 1):
                    if (p == 'P'):
                        val += 1
                    if (p == 'R'):
                        val += 5
                    if (p == 'N'):
                        val += 3
                    if (p == 'B'):
                        val += 3
                    if (p == 'K'):
                        val += 100
                    if (p == 'Q'):
                        val += 9
                else:
                    if (p == 'p'):
                        val -= 1
                    if (p == 'r'):
                        val -= 5
                    if (p == 'n'):
                        val -= 3
                    if (p == 'b'):
                        val -= 3
                    if (p == 'k'):
                        val -= 100
                    if (p == 'q'):
                        val -= 9
    return val

def convert_square(square):
    move = []
    m = ""
    move.append(chr((7 - int(square[1])) + 97))
    move.append(str(int(square[0]) + 1))
    return (m.join(move))

def piece_map_move(chessboard, clr):
    move_dict = {}
    for r in range(0,8):
        for c in range(0,8):
            p = chessboard[r][c]
            if (p != '+'):
                if (piece_color(p) == clr):
                    if ((p == 'p') or (p == 'P')):
                        move_dict[convert_square([r,c])] = pawn_moves(chessboard, r, c)
                    if ((p == 'n') or (p == 'N')):
                        move_dict[convert_square([r,c])] = knight_moves(chessboard, r, c)
                    if ((p == 'k') or (p == 'K')):
                        move_dict[convert_square([r,c])] = king_moves(chessboard, r, c)
                    if ((p == 'b') or (p == 'B')):
                        move_dict[convert_square([r,c])] = bishop_moves(chessboard, r, c)
                    if ((p == 'r') or (p == 'R')):
                        move_dict[convert_square([r,c])] = rook_moves(chessboard, r, c)
                    if ((p == 'q') or (p == 'Q')):
                        move_dict[convert_square([r,c])] = queen_moves(chessboard, r, c)
    return move_dict
