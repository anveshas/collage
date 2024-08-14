def custom_filter(function, lst):
    return [item for item in lst if function(item)]

nums = [1, 2, 3, 4, 5]
result = custom_filter(lambda x: x % 2 == 0, nums)
print(result)