# madlibs.py - Replaces words in a text file with user input

import re

# Read the original text file
with open('madlibs.txt', 'r') as file:
    text = file.read()

# Pattern for words to replace
pattern = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

# Find all placeholders in order
matches = pattern.findall(text)

# Replace each placeholder one by one
for word in matches:
    user_input = input(f'Enter a {word.lower()}: ')
    text = text.replace(word, user_input, 1)

# Print final result
print('\nFinal text:\n')
print(text)

# Save to a new file
with open('madlibs_result.txt', 'w') as file:
    file.write(text)
