from algs4.fundamentals.java_helper import java_string_hash
from HashPipe import HashPipe, Pipe

h = HashPipe()
A = Pipe('A', 2, 1)
C = Pipe('C', 4, 1)
E = Pipe('E', 1, 1)
H = Pipe('H', 5, 4)
R = Pipe('R', 3, 2)
S = Pipe('S', 0, 1)

h.root.references[0] = A
h.root.references[1] = H
h.root.references[2] = H
h.root.references[3] = H

A.references[0] = C
C.references[0] = E
E.references[0] = H
H.references[0] = R
H.references[1] = R
R.references[0] = S

# print(h.current_pipe('S'))
# print(h.get('H'))
# print(h.get('A'))
#print(h.control('C', 0))
#h.put('X', 7)
#h.put('P', 10)

# print(h.find('P').references)


test = HashPipe()
for i, value in enumerate('SEARCHEXAMPLE'):
    test.put(value, i)

node = test.root

while node:
    print(node.references)
    node = node.references[0]


print(test.find('X').references)
