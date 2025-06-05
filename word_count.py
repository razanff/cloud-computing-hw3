# word_count.py

from collections import Counter

with open("abc.txt", "r") as file:
    text = file.read().lower()

words = text.split()
count = Counter(words)

for word, freq in count.items():
    print(f"{word}: {freq}")
