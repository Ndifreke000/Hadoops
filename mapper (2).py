##!/usr/bin/env python

import sys

# Read years to analyze from years.txt
with open('years.txt') as f:
    years_to_analyze = [int(year.strip()) for year in f.readlines() if year.strip()]

# Read genres to analyze from genres.txt
with open('genres.txt') as f:
    genres_to_analyze = [genre.strip() for genre in f.readlines() if genre.strip()]

# Process input from stdin
for line in sys.stdin:
    line = line.strip()
    if line:
        # Split line into components
        parts = line.split('\t')
        if len(parts) == 5:
            reviewer_id, movie_title, genres, year, rating = parts
            
            # Check if year should be analyzed
            if years_to_analyze and int(year) not in years_to_analyze:
                continue
            
            # Split genres if multiple and check if genre should be analyzed
            movie_genres = genres.split('|')
            if genres_to_analyze and not any(genre in genres_to_analyze for genre in movie_genres):
                continue
            
            # Emit key-value pairs (year, movie_title) -> (rating, 1)
            print(f"{year}\t{movie_title}\t{rating}\t1")
