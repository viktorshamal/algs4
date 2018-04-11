from algs4.fundamentals.java_helper import java_string_hash, trailing_zeros


class HashPipe:
    def __init__(self):
        self.root = Pipe(None, None, 32)
        self.size = 0

    def get(self, key):
        pipe = self.find(key)
        return pipe.value if pipe else None

    def put(self, key, value):
        height = trailing_zeros(java_string_hash(key)) + 1
        new_pipe = Pipe(key, value, height)

        references_filled = 0
        current_key = key

        while references_filled < height:
            floor = self.floor(current_key)

            for i, _ in enumerate(floor.references[references_filled:height]):
                new_pipe.references[i] = floor.references[i]
                floor.references[i] = new_pipe
                references_filled += 1

            current_key = floor.key

        self.size += 1

    def control(self, key, height):
        pipe = self.find(key)

        if pipe and len(pipe.references) > height:
            reference = pipe.references[height]
            return reference.key if reference else None
        else:
            return None

    def find(self, key, highest_before=False):
        location = self.root

        while True:
            if location.key == key:
                return location

            if not location.references[0] or location.references[0].key > key:
                if highest_before:
                    return location
                else:
                    return None

            for reference in reversed(location.references):
                if not reference:
                    continue
                if reference.key <= key:
                    location = reference
                    break

    def floor(self, key):
        return self.floor_pipe(key).key

    def floor_pipe(self, key):
        return self.find(key, highest_before=True)


class Pipe:
    def __init__(self, key, value, height):
        self.key = key
        self.value = value
        self.references = [None] * height

    def __repr__(self):
        return self.key


h = HashPipe()
A = Pipe('A', 2, 1)
C = Pipe('C', 4, 1)
E = Pipe('E', 1, 1)
H = Pipe('H', 5, 4)
R = Pipe('R', 3, 2)
S = Pipe('S', 0, 1)

h.root.references = [A, H, H, H]

A.references[0] = C
C.references[0] = E
E.references[0] = H
H.references[0] = R
H.references[1] = R
R.references[0] = S

print(h.floor('X'))
# print(h.get('H'))
# print(h.get('A'))
#print(h.control('C', 0))
#h.put('X', 7)
#h.put('P', 10)

# print(h.find('P').references)

print(h.floor('E'))
