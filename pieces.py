from graphics import *
#starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
move_list = []

# 2 is black, 1 is white, 0 is empty
def piece_color(p):
    if (p < 0):
        return 0
    else:
        if (p > 0):
            return 1
        else:
            return 2

def add_move(r0, c0, r1, c1, clr, sq_clr):
    if (sq_clr == 2):
        temp_list = []
        temp_list.append(r0)
        temp_list.append(c0)
        temp_list.append(r1)
        temp_list.append(c1)
        move_list.append(temp_list)
        return False
    else:
        if (sq_clr != clr):
            temp_list = []
            temp_list.append(r0)
            temp_list.append(c0)
            temp_list.append(r1)
            temp_list.append(c1)
            move_list.append(temp_list)
            return True
        else:
            return True

def rook_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    r+=1
    while (r < 8):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        r+=1
    r = row
    r-=1
    while (r >= 0):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        r-=1
    r = row
    c+=1
    while (c < 8):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        c+=1
    c = col
    c-=1
    while (c >= 0):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
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
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        r+=1
        c+=1
    r = row
    c = col
    r+=1
    c-=1
    while((r < 8) and (c >= 0)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        r+=1
        c-=1
    r = row
    c = col
    r-=1
    c+=1
    while((r >= 0) and (c < 8)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
            break
        r-=1
        c+=1
    r = row
    c = col
    r-=1
    c-=1
    while((r >= 0) and (c >= 0)):
        sq_clr = piece_color(chessboard[r][c])
        if(add_move(row, col, r, c, clr, sq_clr)):
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
        add_move(row, col, r + 2, c + 1, clr, sq_clr)
    if ((r + 1 < 8) and (c + 2 < 8 )):
        sq_clr = piece_color(chessboard[r+1][c+2])
        add_move(row, col, r + 1, c + 2, clr, sq_clr)
    if ((r + 2 < 8) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r+2][c-1])
        add_move(row, col, r + 2, c - 1, clr, sq_clr)
    if ((r + 1 < 8) and (c - 2 >= 0)):
        sq_clr = piece_color(chessboard[r+1][c-2])
        add_move(row, col, r + 1, c - 2, clr, sq_clr)
    if ((r - 2 >= 0) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r-2][c-1])
        add_move(row, col, r - 2, c - 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c - 2 >= 0)):
        sq_clr = piece_color(chessboard[r-1][c-2])
        add_move(row, col, r - 1, c - 2, clr, sq_clr)
    if ((r - 2 >= 0) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r-2][c+1])
        add_move(row, col, r - 2, c + 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c + 2 < 8)):
        sq_clr = piece_color(chessboard[r-1][c+2])
        add_move(row, col, r - 1, c + 2, clr, sq_clr)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def queen_moves(chessboard, row, col):
    b_list = bishop_moves(chessboard, row, col)
    r_list = rook_moves(chessboard, row, col)
    return(b_list + r_list)

def pawn_add_move(r0, c0, r1, c1):
    temp_list = []
    temp_list.append(r0)
    temp_list.append(c0)
    temp_list.append(r1)
    temp_list.append(c1)
    move_list.append(temp_list)

def pawn_moves(chessboard, row, col):
    color = piece_color(chessboard[row][col])
    r = row
    c = col
    if (color == 1):
        if ((r + 1 < 8) and (c + 1 < 8)):
            p = piece_color(chessboard[r + 1][c + 1])
            if ((p != color) and (p != 2)):
                pawn_add_move(row, col, r + 1, c + 1)
        if ((r + 1 < 8) and (c - 1 >= 0)):
            p = piece_color(chessboard[r + 1][c - 1])
            if ((p != color) and (p != 2)):
                pawn_add_move(row, col, r + 1, c - 1)
        if (r + 1 < 8):
            p = piece_color(chessboard[r + 1][c])
            if (p == 2):
                pawn_add_move(row, col, r + 1, c)
                if (row == 1):
                    p1 = piece_color(chessboard[r + 2][c])
                    if (p1 == 2):
                        pawn_add_move(row, col, r + 2, c)
    else:
        if ((r - 1 >= 0) and (c + 1 < 8)):
            p = piece_color(chessboard[r - 1][c + 1])
            if ((p != color) and (p != 2)):
                pawn_add_move(row, col, r - 1, c + 1)
        if ((r - 1 >= 0) and (c - 1 >= 0)):
            p = piece_color(chessboard[r - 1][c - 1])
            if ((p != color) and (p != 2)):
                pawn_add_move(row, col, r - 1, c - 1)
        if (r - 1 >= 0):
            p = piece_color(chessboard[r - 1][c])
            if (p == 2):
                pawn_add_move(row, col, r - 1, c)
                if (row == 6):
                    p1 = piece_color(chessboard[r - 2][c])
                    if (p1 == 2):
                        pawn_add_move(row, col, r - 2, c)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def king_moves(chessboard, row, col):
    clr = piece_color(chessboard[row][col])
    r = row
    c = col
    if ((r + 1 < 8) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r+1][c+1])
        add_move(row, col, r + 1, c + 1, clr, sq_clr)
    if ((r + 1 < 8) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r+1][c-1])
        add_move(row, col, r + 1, c - 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c + 1 < 8)):
        sq_clr = piece_color(chessboard[r-1][c+1])
        add_move(row, col, r - 1, c + 1, clr, sq_clr)
    if ((r - 1 >= 0) and (c - 1 >= 0)):
        sq_clr = piece_color(chessboard[r-1][c-1])
        add_move(row, col, r - 1, c - 1, clr, sq_clr)
    if (r + 1 < 8):
        sq_clr = piece_color(chessboard[r+1][c])
        add_move(row, col, r + 1, c , clr, sq_clr)
    if (r - 1 >= 0):
        sq_clr = piece_color(chessboard[r-1][c])
        add_move(row, col, r - 1, c , clr, sq_clr)
    if (c + 1 < 8):
        sq_clr = piece_color(chessboard[r][c+1])
        add_move(row, col, r , c + 1, clr, sq_clr)
    if (c - 1 >= 0):
        sq_clr = piece_color(chessboard[r][c-1])
        add_move(row, col, r , c - 1, clr, sq_clr)
    m_list = move_list[:]
    move_list.clear()
    return m_list

def piece_map_move(chessboard, clr):
    all_moves = []
    for r in range(0,8):
        for c in range(0,8):
            p = chessboard[r][c]
            #print(piece_color(p),"vs",clr)
            if (p != 0):
                if (piece_color(p) == clr):
                    p = abs(p)
                    if (p == 4):
                        all_moves += pawn_moves(chessboard, r, c)
                    if (p == 12):
                        all_moves += knight_moves(chessboard, r, c)
                    if (p == 100000):
                        all_moves += king_moves(chessboard, r, c)
                    if (p == 13):
                        all_moves += bishop_moves(chessboard, r, c)
                    if (p == 20):
                        all_moves += rook_moves(chessboard, r, c)
                    if (p == 36):
                        all_moves += queen_moves(chessboard, r, c)
    return all_moves




# converts coord to letter square [3, 3] -> e4
def convert_square(square):
    move = []
    m = ""
    move.append(chr((7 - int(square[1])) + 97))
    move.append(str(int(square[0]) + 1))
    return (m.join(move))







#
