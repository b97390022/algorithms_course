# Course2-Week1-Kosaraju algorithm
import copy
import os
from collections import Counter
from collections import deque


def DFS_loop_iter(G, order_list):
    ord = deque()
    stack = deque()

    for i in order_list:
        if not G[i][1]:
            stack.append(i)

            while len(stack) > 0:
                p = stack[-1]
                G[p][1] = True
                # print(p,stack)
                flag = True
                for child in G[p][0]:
                    if not G[child][1]:
                        stack.append(child)
                        G[child][1] = True
                        flag = False

                if flag:
                    ord.appendleft(p)
                    G[p][2] = i
                    stack.pop()

    t = [G[i][2] for i in G]

    return ord, t


if __name__ == "__main__":

    # file_path = r'/content/drive/MyDrive/kosaraju.txt'
    file_path = os.path.abspath(os.getcwd()) + r"\txt files\kosaraju.txt"

    with open(
        file_path,
        mode="r",
    ) as f:
        lines = f.readlines()

    node_1 = [int(line.split(" ")[:-1][0]) for line in lines]
    node_2 = [int(line.split(" ")[:-1][-1]) for line in lines]
    nodes = set(node_1 + node_2)

    keys_edges_foward = [*range(1, len(nodes) + 1, 1)]
    keys_edges_reverse = [*range(1, len(nodes) + 1, 1)]

    dict_edges_foward = {key: [[], False, 0] for key in keys_edges_foward}
    dict_edges_reverse = {key: [[], False, 0] for key in keys_edges_reverse}

    for i, line in enumerate(lines):
        edges = line.split(" ")[:-1]

        if int(edges[0]) in dict_edges_foward:
            dict_edges_foward[int(edges[0])][0].append(int(edges[-1]))
        else:
            dict_edges_foward[int(edges[0])] = [[int(edges[-1])], False, 0]

        if int(edges[-1]) in dict_edges_reverse:
            dict_edges_reverse[int(edges[-1])][0].append(int(edges[0]))
        else:
            dict_edges_reverse[int(edges[-1])] = [[int(edges[0])], False, 0]

    dict_edges_foward_deep = copy.deepcopy(dict_edges_foward)
    dict_edges_reverse_deep = copy.deepcopy(dict_edges_reverse)

    ord, t = DFS_loop_iter(dict_edges_reverse_deep, [*range(len(nodes), 0, -1)])

    ord, t = DFS_loop_iter(dict_edges_foward_deep, ord)

    print(f"Answer: {Counter(t).most_common(5)}")
