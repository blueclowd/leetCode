'''
Description:
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''

from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        q = PriorityQueue()

        for point in points:
            q.put((point[0] ** 2 + point[1] ** 2, point))

        result = []
        for index in range(K):
            result.append(q.get()[1])

        return result