def triplet(n):
    return [(a, b, a+b) for a in range(1, n) for b in range(a, n) if a + b < n]

print(triplet(10))