#!/usr/bin/env python3

import sys
from collections import defaultdict

word_counts = defaultdict(int)

for line in sys.stdin:
    word, count = line.strip().split('\t')
    word_counts[word] += int(count)

top3 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

for word, count in top3:
    print(f"{word}\t{count}")
