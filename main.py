from logic import *
from pieces import *
from graphics import *
import copy
def move_to_coord(move):
    m_list = []
    m_list.append(ord(move[1]) - ord('1'))
    m_list.append((ord(move[0]) - ord('h')) * -1)
    return m_list

def see_moves(moves):
    for m in moves:
        print(convert_square(m))

def move_parse(move):
    m_list = []
    m_list.append(ord(move[1]) - ord('1'))
    m_list.append((ord(move[0]) - ord('h')) * -1)
    m_list.append(ord(move[3]) - ord('1'))
    m_list.append((ord(move[2]) - ord('h')) * -1)
    return m_list

fen = "8/5k2/4ppp1/3p4/8/3B4/3K4/8"
#rook_moves(chessboard,move_to_coord("e4")[0],move_to_coord("e4")[1])
square = "f7"
#see_moves(pawn_moves(setup_board(fen[::-1]), move_to_coord(square)[0],move_to_coord(square)[1]))
#print(total_value(setup_board(fen[::-1])))

n1 = Position(setup_board(fen[::-1]), 0)

def to_fen(cb):
    s = ''
    b = []
    co = 0
    for r in reversed(range(8)):
        for c in reversed(range(8)):
            p = cb[r][c]
            if (p == '+'):
                co+=1
            else:
                if (co > 0):
                    b.append(str(co))
                    co = 0
                b.append(cb[r][c])
        if (co > 0):
            b.append(str(co))
        co = 0
        b.append("/")
    return (s.join(b))

def bfs(nn, layer):
    if (layer < 4):
        front = []
        m_dict = piece_map_move(nn.cb, (1 if (layer % 2 == 0) else 2))
        for piece in m_dict:
            for mv in m_dict[piece]:
                plist = move_to_coord(piece)
                cb = nn.cb
                cb[ mv[0] ][ mv[1] ] = cb[plist[0]][plist[1]]
                cb[plist[0]][plist[1]] = '+'
                new_node = Position(cb, nn)
                front.append(new_node)
        nn.front = front
        for i in front:
            bfs(i, layer + 1)
    else:
        nn.total = total_value(nn.cb)
        print(total_value(nn.cb))
        return nn

bfs(n1, 0)
print("Finished tree")
print(n1.front)
traverse(n1, 2)
print(n1.total)