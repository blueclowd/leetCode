'''
Description:
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
Also, there is no garden that has more than 3 paths coming into or leaving it.
Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
'''

from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for node_1, node_2 in paths:
            graph[node_1 - 1].append(node_2 - 1)
            graph[node_2 - 1].append(node_1 - 1)

        colors = [0] * N

        for node in range(N):

            adj_nodes = graph[node]

            used_colors = [colors[adj_node] for adj_node in adj_nodes]

            for i in range(1, 5):

                if i not in used_colors:
                    colors[node] = i
                    break

        return colors