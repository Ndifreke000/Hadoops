#!/usr/bin/env python

import sys

current_key = None
current_rating_sum = 0
current_count = 0

# Process input from stdin
for line in sys.stdin:
    line = line.strip()
    if line:
        key, rating, count = line.split('\t')
        rating = float(rating)
        count = int(count)
        
        # If the key changes (or first entry), emit the aggregated result
        if current_key and current_key != key:
            print(f"{current_key}\t{current_rating_sum}\t{current_count}")
            current_rating_sum = 0
            current_count = 0
        
        current_key = key
        current_rating_sum += rating * count
        current_count += count

# Don't forget to emit the last key
if current_key:
    print(f"{current_key}\t{current_rating_sum}\t{current_count}")
