from logic import *
from pieces import *
from graphics import *
import copy

'''
Redundant functions:
move_to_coord()
see_moves
'''

# takes a square "e4" and turns into a coordinate array [3, 3]
def move_to_coord(move):
    m_list = []
    m_list.append(ord(move[1]) - ord('1'))
    m_list.append((ord(move[0]) - ord('h')) * -1)
    return m_list

#used in conjunction with move_to_coord() to see all possible moves
def see_moves(moves):
    for m in moves:
        print(convert_square([m[2],m[3]]))

#takes a move "e2e4" and turns it into an array [1, 3, 3, 3]
def move_parse(move):
    m_list = []
    m_list.append(ord(move[1]) - ord('1'))
    m_list.append((ord(move[0]) - ord('h')) * -1)
    m_list.append(ord(move[3]) - ord('1'))
    m_list.append((ord(move[2]) - ord('h')) * -1)
    return m_list

# fen = "8/8/8/5k2/R1R1q3/1K6/8/8"
# starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# #rook_moves(chessboard,move_to_coord("e4")[0],move_to_coord("e4")[1])
# square = "f7"
# #see_moves(pawn_moves(setup_board(fen[::-1]), move_to_coord(square)[0],move_to_coord(square)[1]))

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
chessboard = setup_board(fen[::-1])
#print(knight_moves(chessboard,move_to_coord("e4")[0],move_to_coord("e4")[1]))
#print(convert_square([3,3]))

n1 = Position(setup_board(fen[::-1]), 0, 0, 0)
traverse(n1, 1, 0)
#print_board((n1.front)[4].cb)

# mv = (piece_map_move(n1.cb, 1))
# make_move(n1.cb, mv)
# print_board(n1.cb)

#print(convert_square([mv[0],mv[1]])+convert_square([mv[2],mv[3]]))































# n1 = Position(setup_board(fen[::-1]), 0, 0)
# def to_fen(cb):
#     s = ''
#     b = []
#     co = 0
#     for r in reversed(range(8)):
#         for c in reversed(range(8)):
#             p = cb[r][c]
#             if (p == '+'):
#                 co+=1
#             else:
#                 if (co > 0):
#                     b.append(str(co))
#                     co = 0
#                 b.append(cb[r][c])
#         if (co > 0):
#             b.append(str(co))
#         co = 0
#         b.append("/")
#     return (s.join(b))
#
# def bfs(nn, layer):
#     if (layer < 4):
#         front = []
#         m_dict = piece_map_move(nn.cb, (1 if (layer % 2 == 0) else 2))
#         if(bool(m_dict)):
#             for piece in m_dict:
#                 for mv in m_dict[piece]:
#                     next_move = (piece+convert_square(mv))
#                     plist = move_to_coord(piece)
#                     cb = nn.cb
#                     cb[ mv[0] ][ mv[1] ] = cb[plist[0]][plist[1]]
#                     cb[plist[0]][plist[1]] = '+'
#                     new_node = Position(cb, nn, next_move)
#                     front.append(new_node)
#             nn.front = front
#             for i in front:
#                 bfs(i, layer + 1)
#         else:
#             nn.total = total_value(nn.cb)
#             return nn
#     else:
#         nn.total = total_value(nn.cb)
#         return nn
#
# bfs(n1, 0)
# traverse(n1, 2)
