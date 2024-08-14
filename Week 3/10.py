import textwrap

def wrap_lines(filename, width):
    with open(filename, 'r') as file:
        lines = file.readlines()
    wrapped_lines = [textwrap.fill(line, width) for line in lines]
    with open(filename, 'w') as file:
        file.writelines(wrapped_lines)

filename = 'example.txt'
wrap_lines(filename, 40)