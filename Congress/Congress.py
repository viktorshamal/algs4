import heapq
from math import sqrt
from collections import namedtuple
from sys import stdin

def geometric_mean(n):
    return sqrt(n * (n+1))

def apport():
    heap = []
    
    next(stdin) # skip over states
    seats = int(stdin.readline())

    State = namedtuple('State', ['pop','orgpop','seats','name'])
    
    while True:
        name = stdin.readline().strip()
        population = stdin.readline().strip()

        if population:
            orgpop = -1 * int(population)
            pop = orgpop / geometric_mean(1)
            entry = State(pop, orgpop, 1, name)
            heapq.heappush(heap, entry)
        else:
            break

    for _ in range(seats - len(heap)):
        largest = heap[0]
        new_seats = largest.seats + 1
        reduced_pop = largest.orgpop / geometric_mean(new_seats)
        new_state = State(reduced_pop, largest.orgpop, new_seats, largest.name)
        heapq.heapreplace(heap, new_state)

    for state in heap:
        print(state.name, state.seats)

apport()