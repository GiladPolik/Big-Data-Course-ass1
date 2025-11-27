#!/usr/bin/env python3


import sys
import string

def clean_word(word: str) -> str:
    return word.lower().strip(string.punctuation)

for line in sys.stdin:
    for word in line.split():
        word = clean_word(word)
        if word:
            print(f"{word}\t1")
