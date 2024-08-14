def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(group(my_list, 3)) 