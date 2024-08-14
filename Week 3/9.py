def reverse_each_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.rstrip()[::-1])

filename = 'example.txt'
reverse_each_line(filename)