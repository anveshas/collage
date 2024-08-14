def parse_csv(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

filename = 'data.csv'
print(parse_csv(filename))
def mutate(word):
    from string import ascii_lowercase

    mutations = []
    for i in range(len(word)):
        for c in ascii_lowercase:
            mutations.append(word[:i] + c + word[i:])

        mutations.append(word[:i] + word[i+1:])

        for c in ascii_lowercase:
            mutations.append(word[:i] + c + word[i+1:])

    for i in range(len(word) - 1):
        mutations.append(word[:i] + word[i+1] + word[i] + word[i+2:])
    return list(set(mutations))

word = 'cat'
print(mutate(word))
