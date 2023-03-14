import hunspell
from itertools import combinations_with_replacement, permutations
import random

h = hunspell.Hunspell()
# get today's letters
letters = input("What are today's letters? ").lower()
while (len(letters) != 7) or (len(letters) != len(set(letters))) or (not letters.isalpha()):
    print('Puzzle must contain 7 distinct letters.')
    letters = input("What are today's letters? ").lower()

central = input("Central letter: ").lower()
while (len(central) != 1) or (not central.isalpha()):
    print('Enter only a single letter.')
    central = input("Central letter: ").lower()
while central not in letters:
    print('Central letter must be one of the 7 total letters.')
    central = input("Central letter: ").lower()

start = input('First letter: ').lower()
while (len(start) != 1) or (not start.isalpha()):
    print('Enter only a single letter.')
    start = input("First letter: ").lower()
while start not in letters:
    print('First letter must be one of the 7 total letters.')
    start = input('First letter: ').lower()

length = input("Word length: ")
while (not length.isnumeric()):
    print('Enter only a single number.')
    length = input("Word length: ")
while int(length) <= 4:
    print('Enter a number greater than or equal to 4.')
    length = input("Word length: ")

difficulty = input('Hard or easy? ').lower()
while difficulty not in ['hard','easy']:
    difficulty = input('Hard or easy? ').lower()

print('Inputs accepted.')

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
print(f'{len(words)}, {length}-letter word(s) starting with {start.upper()}:')

if difficulty == 'hard':
    for word in words:
        idx_to_reveal = random.sample(range(1, len(word)), round(len(word)/2 - 1))
        modified_word = []

        for i in range(len(word)):
            if i == 0 or i in idx_to_reveal:
                modified_word.append(word[i])
            else:
                modified_word.append('_')
        print(''.join(modified_word))
else:
    for word in words:
        print(word)
