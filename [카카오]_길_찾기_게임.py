import sys
sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    x = []
    y = []
    graph = [(i + 1, v) for i, v in enumerate(nodeinfo)]
    print(graph)

    def recursion(nodes):
        nodes.sort(key = lambda x: -x[1][1])
        if len(nodes) == 1:
            x.append(nodes[0][0])
            y.append(nodes[0][0])
        else:
            y.append(nodes[0][0])
            left_graph = [x for x in nodes if x[1][0] < nodes[0][1][0]]
            right_graph = [x for x in nodes if x[1][0] > nodes[0][1][0]]
            if left_graph:
                recursion(left_graph)
            if right_graph:
                recursion(right_graph)
            x.append(nodes[0][0])

    recursion(graph)
    return [y, x]
