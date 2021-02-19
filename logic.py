from pieces import *
class Position:
    def __init__(self, cb, back):
        self.cb = cb
        self.total = '+'
        self.vals = []
        self.back = back
        self.front = []
        self.pruned = False
        self.temp = 0

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

def traverse(node, color):
    if (node.front):
        for child in (node.front):
            prune(child, color)
            if (not node.pruned):
                node.vals.append(traverse(child, color + 1))
            else:
                node.total = node.temp
                return (node.total)
        print(node.vals)
        if (color % 2 == 0):
            node.total = min(node.vals)
            return (node.total)
        else:
            node.total = max(node.vals)
            return (node.total)
    else:
        return (node.total)

def choose_move(node):
    i = 0
    for n in (node.front):
        if (n.total == node.total):
            return i
        i+=1
