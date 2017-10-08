
from collections import Counter

words = Counter()

with open('capitals.txt') as handle:
    text = handle.read()
    text = text.replace("\n", " ")
    words.update(text.split(' '))

print(words.most_common(20))
