import sys
from algs4.stdlib import stdio
from algs4.fundamentals.uf import WeightedQuickUnionUF
 
# Reads in a an integer n and a sequence of pairs of integers
# (between 0 and n-1) from standard input or a file
# supplied as argument to the program, where each integer
# in the pair represents some site; if the sites are in different
# components, merge the two components and print the pair to standard output.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    n = stdio.readInt()
    uf = WeightedQuickUnionUF(n)
    while not stdio.isEmpty():
        p = stdio.readInt()
        q = stdio.readInt()
        if uf.connected(p, q):
            continue
        uf.union(p, q)
    print(uf.connected(0, 1))