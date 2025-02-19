import sys
sys.stdin = open("input.txt")


def set_tree(node, height):
    global node_list
    node.height = height
    node.subtree_size = 1
    if not node.child:
        return 1
    else:
        for child in node.child:
            node.subtree_size += set_tree(node_list[child], height + 1)
        return node.subtree_size


T = int(input())

class Node:
    def __init__(self, idx, parent, child):
        self.idx = idx
        self.parent = parent
        self.child = child
        self.height = None
        self.subtree_size = None

for idx in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    node_list = [Node(i, [], []) for i in range(V + 1)]
    edge_list = list(map(int, input().split()))

    for i in range(0, 2 * E - 1, 2):
        node_list[edge_list[i]].child.append(edge_list[i + 1])
        node_list[edge_list[i + 1]].parent.append(edge_list[i])
    
    set_tree(node_list[1], 0)
    
    if node_list[a].height < node_list[b].height:
        a, b = b, a
    
    while node_list[a].height != node_list[b].height:
        a = node_list[a].parent[0]
    
    while a != b:
        a = node_list[a].parent[0]
        b = node_list[b].parent[0]
    
    print("#{}".format(idx), a, node_list[a].subtree_size)