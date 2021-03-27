import numpy
import hashlib
from pieces import *
from graphics import *
class Position:
    def __init__(self, cb, back, move, piece):
        self.cb = cb
        self.total = '+'
        self.vals = []
        self.back = back
        self.front = []
        self.pruned = False
        self.temp = 0
        self.move = move
        self.piece = 0
        self.enpassant = False
        self.castle = True

def to_fen(cb):
    s = ''
    b = []
    co = 0
    for r in reversed(range(8)):
        for c in reversed(range(8)):
            p = cb[r][c]
            if (p == 0):
                co+=1
            else:
                if (co > 0):
                    b.append(str(co))
                    co = 0
                b.append(num_to_letter(cb[r][c]))
        if (co > 0):
            b.append(str(co))
        co = 0
        b.append("/")
    return (s.join(b))

def make_move(chessboard, move):
    if (move[0] == 'p'):
        pass
    elif (move[0] == 'c'):
        pass
    elif (move[0] == 'e'):
        pass
    else:
        chessboard[move[2]][move[3]] = chessboard[move[0]][move[1]]
        chessboard[move[0]][move[1]] = 0
    return chessboard

def reverse_position(chessboard, move, piece):
    if (move == 0):
        pass
    elif(move[0] >=0 and move[0] <= 7):
        chessboard[move[0]][move[1]] = chessboard[move[2]][move[3]]
        chessboard[move[2]][move[3]] = piece
    elif (move[0] == 'p'):
        pass
    elif (move[0] == 'c'):
        pass
    elif (move[0] == 'e'):
        pass
    return chessboard

def prune(node, color):
    value = node.total
    temp_node = node
    new_node = node.back
    to_prune = False
    p_list = []
    new_color = color
    if (new_node != 0):
        while (new_node.back != 0):
            if (value != '+'):
                i = 0
                while ((new_node.back.front)[i] != new_node):
                    if ((new_node.back.front)[i].total != '+'):
                        p_list.append(new_node)
                        p_list.append(temp_node)
                        if (new_color % 2 == 0):
                            if (value < (new_node.back.front)[i].total):
                                to_prune = True
                        else:
                            if (value > (new_node.back.front)[i].total):
                                to_prune = True
                    new_node.temp = value
                    i += 1
            new_color += 1
            if (new_node.back == 0):
                break
            else:
                new_node = new_node.back
                temp_node = temp_node.back
    for p in p_list:
        if (to_prune):
            p.pruned = True

def traverse(node, color, depth):
    color = color % 2
    if (depth < 6):
        print("-----------------------------")
        print("Depth:",depth)
        pos = to_fen(node.cb)
        enc = pos.encode()
        #print((hashlib.sha256(enc)).hexdigest())
        print("\n\n")
        print_board(node.cb)
        print("-----------------------------")

        for move in (piece_map_move(node.cb, color)):
            moved_piece = (node.cb)[move[2]][move[3]]
            child = Position(make_move(node.cb, move), node, move, moved_piece)
            (node.front).append(child)
            #print()
            prune(child, color)
            if (not node.pruned):
                node.vals.append(traverse(child, color + 1, depth + 1))
            else:
                node.total = node.temp
                reverse_position(node.cb, node.move, node.piece)
                return (node.total)
        if (color == 0):
            node.total = min(node.vals)
            return (node.total)
        else:
            node.total = max(node.vals)
            return (node.total)
    else:
        reverse_position(node.cb, node.move, node.piece)
        node.total = numpy.sum(numpy.sum(node.cb))
        return node.total

def choose_move(node):
    i = 0
    for n in (node.front):
        if (n.total == node.total):
            return i
        i+=1












#
