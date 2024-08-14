with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.writelines(["This is the first line.\n", "This is the second line.\n"])

with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:\n", content)

with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)
    second_line = file.readline()
    print("Second line:", second_line)
