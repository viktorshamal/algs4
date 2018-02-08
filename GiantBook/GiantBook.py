"""A client that searches for giant components in a network"""
from MyUnionFind import MyUnionFind
from random import randint


class GiantBook:
    def __init__(self, count):
        self.count = count
        self.store = MyUnionFind(count)
        self.giantComponent = False

    def checkGiantComponent(self, i):
        n_half = int(self.count * 0.5)

        if not self.giantComponent and self.store.maxComponentSize > n_half:
            self.giantComponent = i


w
    def simulateRandomConnections(self):
        i = 0

        while True:
            p = randint(0, self.count - 1)
            q = randint(0, self.count - 1)

            if not self.store.connected(p, q):
                self.store.union(p, q)

            self.checkGiantComponent(i)

            i += 1

            if self.store.count() == 1:
                break

        print(self.count, self.giantComponent)


g = GiantBook(int(1e5))
g.simulateRandomConnections()
