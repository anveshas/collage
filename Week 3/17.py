def find_anagrams(words):
    sorted_words = [''.join(sorted(word)) for word in words]
    anagrams = {}
    for word, sorted_word in zip(words, sorted_words):
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return [group for group in anagrams.values() if len(group) > 1]

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(find_anagrams(words)) 