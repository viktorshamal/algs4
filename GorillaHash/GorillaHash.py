from algs4.fundamentals.java_helper import java_string_hash

k = 20
d = 10000


def hash(s):
    return java_string_hash(s) % d


def profile(s):
    for i in range(0, len(s) - k):
        print(hash(s[i:i+k]))


with open('HbB_FASTAs-in.txt', 'r') as f:
    current = ''
    for line in f:
        line = line.strip()
        if line[0] is '>':
            if current:
                print(current)
                p = profile(current)
            current = ''
        else:
            current += line
