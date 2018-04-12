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
        references_filled = 0

        new_pipe = Pipe(key, value, height)
        current_pipe = self.floor_pipe(new_pipe.key)
        next_pipe = current_pipe.references[0]

        if(next_pipe and next_pipe.key == key):
            next_pipe.value = value
            return None

        while references_filled < height:
            interval = current_pipe.references[references_filled:height]

            for i, _ in enumerate(interval, start=references_filled):
                new_pipe.references[i] = current_pipe.references[i]
                current_pipe.references[i] = new_pipe
                references_filled += 1

            current_pipe = self.floor_pipe(current_pipe.key)

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
                    # Lets quit if we're looking for the current_pipe and the next pipe has our key.
                    if highest_before and reference.key == key:
                        return location
                    location = reference
                    break

    def floor_pipe(self, key):
        return self.find(key, highest_before=True)


class Pipe:
    def __init__(self, key, value, height):
        self.key = key
        self.value = value
        self.references = [None] * height

    def __repr__(self):
        return self.key
