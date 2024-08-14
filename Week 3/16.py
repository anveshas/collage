def character_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

filename = 'example.txt'
print(character_frequency(filename))
