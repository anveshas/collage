def lensort(strings):
    return sorted(strings, key=len)

strings = ["apple", "banana", "kiwi", "pear"]
print(lensort(strings))

def extsort(files):
    return sorted(files, key=lambda x: x.split('.')[-1])

files = ["file1.txt", "file2.jpg", "file3.png", "file4.docx"]
print(extsort(files)) 