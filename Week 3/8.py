def reverse_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.rstrip())

filename = 'example.txt'
reverse_lines(filename)
