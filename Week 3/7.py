def file_statistics(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_chars, num_words, num_lines

filename = 'example.txt'
characters, words, lines = file_statistics(filename)
print(f"Characters: {characters}, Words: {words}, Lines: {lines}")
