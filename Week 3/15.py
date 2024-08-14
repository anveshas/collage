def nearly_equal(a, b):
    if len(a) == len(b):
        return sum(1 for x, y in zip(a, b) if x != y) == 1
    elif len(a) == len(b) + 1:
        return any(a[:i] + a[i+1:] == b for i in range(len(a)))
    elif len(b) == len(a) + 1:
        return nearly_equal(b, a)
    return False

print(nearly_equal('cat', 'bat')) 
print(nearly_equal('cat', 'cats'))
print(nearly_equal('cat', 'cut'))
