'''
Description:
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
'''

class Solution:
    def equationsPossible(self, equations) -> bool:

        disjointSet = DisjointSet(26)
        for equation in equations:
            if "!" not in equation:
                disjointSet.union(ord(equation[0]) - ord('a'), ord(equation[-1]) - ord('a'))

        for equation in equations:
            if "!" in equation:

                root_of_a = disjointSet.find(ord(equation[0]) - ord('a'))
                root_of_b = disjointSet.find(ord(equation[-1]) - ord('a'))

                if root_of_a == root_of_b:

                    return False

        return True

class DisjointSet:

    def __init__(self, n):
        self.roots = list(range(n))
        self.sizes = [1] * n

    def find(self, a):

        while self.roots[a] != a:
            a = self.roots[a]
        return a

    def union(self, a, b):

        root_a = self.roots[a]
        root_b = self.roots[b]

        if self.sizes[root_a] < self.sizes[root_b]:
            self.roots[root_a] = self.roots[root_b]
            self.sizes[root_b] += self.sizes[root_a]
        else:
            self.roots[root_b] = self.roots[root_a]
            self.sizes[root_a] += self.sizes[root_b]
