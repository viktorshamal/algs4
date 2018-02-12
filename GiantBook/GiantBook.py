"""A client that searches for giant components in a network"""
from MyUnionFind import MyUnionFind
from random import randint
from math import ceil
from numpy import mean, std


class GiantBook:
    def __init__(self, count):
        self.count = count
        self.store = MyUnionFind(count)
        self.giantComponent = False
        self.isConnected = False

    def simulateRandomConnections(self):
        i = 0
        n_half = ceil(self.count * 0.5)

        while self.store.count() > 1:
            i += 1

            p = randint(0, self.count - 1)
            q = randint(0, self.count - 1)

            # Union first
            if not self.store.connected(p, q):
                self.store.union(p, q)

            # Check for Giant Component
            if not self.giantComponent and self.store.maxComponentSize >= n_half:
                self.giantComponent = i

            # Check for no isolated components
            if not self.isConnected and self.store.isolatedComponents == 0:
                self.isConnected = i

        return self.giantComponent, self.isConnected, i


def performanceTest(N, T):
    results = []

    for t in range(T):
        result = GiantBook(N).simulateRandomConnections()
        results.append(result)

    results = mean(results, axis=0), std(results, axis=0)

    for x in results:
        for y in x:
            print('%.2e' % y)


performanceTest(int(1e9), 1)
