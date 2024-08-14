def duplicate(lst):
    duplicates = []
    seen = set()
    for num in lst:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8]
print(duplicate(numbers))
