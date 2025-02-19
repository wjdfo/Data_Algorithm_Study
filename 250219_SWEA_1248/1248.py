import sys
sys.stdin = open("input.txt")

T = int(input())

class Node:
    def __init__(self, idx, parent, child):
        self.idx = idx
        self.parent = parent
        self.child = child
        self.height = None

for idx in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    node_list = [Node(i, [], []) for i in range(V + 1)]
    edge_list = list(map(int, input().split()))

    for i in range(0, 2 * E - 1, 2):
        node_list[edge_list[i]].child.append(edge_list[i + 1])
        node_list[edge_list[i + 1]].parent.append(edge_list[i])
    print()