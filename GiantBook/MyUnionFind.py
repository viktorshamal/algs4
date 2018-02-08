"""A Union-Find data structure"""
from algs4.fundamentals.uf import WeightedQuickUnionUF as UF


class MyUnionFind(UF):
    def __init__(self, *args, **kwargs):
        super(MyUnionFind, self).__init__(*args, **kwargs)
        self.maxComponentSize = 1
        self.isolatedComponents = self._count

    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p

        # If it's an isolated component being connected,
        # then it's no longer isolated.
        if self._size[small] == 1:
            self.isolatedComponents -= 1
        if self._size[large] == 1:
            self.isolatedComponents -= 1

        self._parent[small] = large
        self._size[large] += self._size[small]

        if self._size[large] > self.maxComponentSize:
            self.maxComponentSize = self._size[large]

        self._count -= 1
