# Course1-Week4-KargerMinCut
import copy
import datetime
import os
import random
import time

import matplotlib.pyplot as plt
import numpy as np


def edges_count(dic):
    c = 0
    for i in dic.keys():
        c += len(dic[i])
    a = [len(v) / c for v in dic.values()]
    return a


def contract(dict_edges, u, v):
    dict_edges[u][:] = (i for i in dict_edges[u] if i != v)
    dict_edges[v][:] = (i for i in dict_edges[v] if i != u)
    dict_edges[u].extend(dict_edges[v])
    del dict_edges[v]
    # dict_edges[vertex][j] = (u for vertex in dict_edges for j, v in enumerate(dict_edges[vertex]) if v == v)
    for vertex in dict_edges:
        for index, neighbor in enumerate(dict_edges[vertex]):
            if neighbor == v:
                dict_edges[vertex][index] = u


def KargarMinCut():
    countMin = 10000
    counts = []

    start = time.time()

    for i in range(500):

        if i % 100 == 0:
            print("-----------------")
            now = time.time() - start
            now = str(datetime.timedelta(seconds=now))
            print(f"Now Loop: {i}, elapsed time: {now}")
            print("-----------------")

        dict_copy = copy.deepcopy(dict_edges)

        while len(dict_copy) > 2:
            edges_list = edges_count(dict_copy)
            # print(edges_list)

            u = np.random.choice(list(dict_copy.keys()), p=edges_list)
            v = dict_copy[u][random.randint(0, len(dict_copy[u]) - 1)]

            contract(dict_copy, u, v)

        count = len(list(dict_copy.values())[0])

        if count < countMin:
            countMin = count

        counts.append(count)

    final = time.time() - start
    print(f"total: {str(datetime.timedelta(seconds=final))}")
    # print(f'countMin now is: {count}, {i} th run')

    return counts, countMin


def drawHist(counts):
    plt.xlabel("MinCount")
    plt.ylabel("times")
    plt.title("Histogram Plot of MinCount")
    plt.hist(counts, bins=range(120))
    plt.show()


if __name__ == "__main__":

    # file_path = r'/content/drive/MyDrive/KargerMinCut.txt'

    file_path = os.path.abspath(os.getcwd()) + r"\txt files\KargerMinCut.txt"

    dict_edges = {}
    dict_vertices = {}

    with open(
        file_path,
        mode="r",
    ) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        edges = line.split("\t")[1:]
        dict_edges[i + 1] = [int(edge) for edge in edges if edge != "\n"]

    counts, countMin = KargarMinCut()

    print(f"countMin = {countMin}")
    drawHist(counts)
