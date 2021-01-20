
def solve(v):
    i, f = 0, len(v)
    while f - i > 1:
        h = i + ((f - i + 1) // 2)
        if v[h - 1] <= v[h]:
            f = h
        elif v[h - 1] > v[h]:
            i = h
    return i, v[i]


v = [11, 4, 5, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

for i in range(1000000):
    v.append(9)

print(solve(v))