import hunspell
from itertools import combinations_with_replacement, permutations
from PyDictionary import PyDictionary

h = hunspell.Hunspell()
# get today's letters
letters = input("What are today's letters? ").lower()
central = input("Central letter: ").lower()
start = input('First letter: ').lower()
length = input("Word length: ")
# good checks on input: num letters should be 7, central must be in letters, length must be a number leq 7
# letters must be all alpha, no spaces or numbers or punctuation

# find all combinations of length `length`
lettergroups = list(combinations_with_replacement(list(letters), int(length)))
# limit to only words with the central letter
lettergroups = [''.join(word) for word in lettergroups if central in ''.join(word)]

words = []
# for each letter group candidates, find all permuatations (no replacement)
for word in lettergroups:
    words.extend(
        permutations(word)
    )

# limit to only actual english words
# note that hunspell has a more efficient, batched + multithreaded way
words = list(set([''.join(word) for word in words if h.spell(''.join(word))]))
words.sort()

"""
# instead of giving away the word, print the definition
# Call PyDictionary class
# dc = PyDictionary()
# tried this; too many bugs in the dictionary.
# missing common words like "that" or "they" and containing many entries for proper nouns 
# still some weird behavior even with hunspell, for example: "theed" is not a word but hunspell says it is 
"""
words = [word for word in words if word[0] == start]
print(f'{len(words)}, {length}-letter words starting with {start.upper()}:')

for word in words:
    print(word)



