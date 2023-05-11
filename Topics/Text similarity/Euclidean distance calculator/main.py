import math


def euclidean_distance(doc_1: list, doc_2: list) -> float:
    distance = 0
    r = 0.0
    for (x, y) in zip(doc_1, doc_2):
        r += math.pow(x - y, 2)
    distance = math.sqrt(r)
    return distance


doc_1 = [int(i) for i in input().split()]
doc_2 = [int(i) for i in input().split()]

print(euclidean_distance(doc_1, doc_2))
