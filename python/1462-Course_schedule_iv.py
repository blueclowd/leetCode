'''
Description:
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]
Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.
You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.
Return a list of boolean, the answers to the given queries.
Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.
'''

from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        records = [[False] * n for i in range(n)]

        for node, child in prerequisites:
            records[node][child] = True

        for i in range(n):

            queue = [i]

            visited = set()

            while queue:

                node = queue.pop(0)

                for j in range(n):

                    if records[node][j] and j not in visited:
                        queue.append(j)
                        visited.add(j)

                        records[i][j] = True

        results = []
        for node, child in queries:
            results.append(records[node][child])

        return results