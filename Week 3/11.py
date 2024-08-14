def custom_map(function, lst):
    return [function(item) for item in lst]

nums = [1, 2, 3, 4]
result = custom_map(lambda x: x * 2, nums)
print(result)