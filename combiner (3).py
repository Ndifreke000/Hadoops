#!/usr/bin/env python3

# Student Number: 3329748
import sys
from collections import defaultdict

movie_ratings = defaultdict(lambda: [0, 0])  # (total rating, count)

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) != 3:
        continue

    year, movie_title, rating = parts
    rating = float(rating)
    
    key = (year, movie_title)
    movie_ratings[key][0] += rating
    movie_ratings[key][1] += 1

for (year, movie_title), (total_rating, count) in movie_ratings.items():
    print(f"{year}\t{movie_title}\t{total_rating}\t{count}")
