'''
Description:
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distance = [[float("inf")] * n for i in range(n)]

        for city_1, city_2, weight in edges:
            distance[city_1][city_2] = weight
            distance[city_2][city_1] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if i == j:
                        continue

                    distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
                    distance[j][i] = distance[i][j]

        counts = []
        for i in range(n):

            within_threshold = 0
            for j in range(n):

                if distance[i][j] <= distanceThreshold:
                    within_threshold += 1

            counts.append(within_threshold)

        minimum_city_index = -1
        minimum_city_distance = float("inf")
        for i in range(n):

            if counts[i] <= minimum_city_distance:
                minimum_city_index = i
                minimum_city_distance = counts[i]

        return minimum_city_index
