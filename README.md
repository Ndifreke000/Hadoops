# Movie Ratings Analysis using Hadoop MapReduce

## Project Description

This project analyzes a large dataset of movie ratings to find the film title(s) with the highest average rating for each year, for a specified set of years and genres. The dataset contains over 100,000 ratings from a group of reviewers. The project is implemented using Hadoop MapReduce, with Python scripts for the mapper, combiner, and reducer stages.

## Directory Structure

```plaintext
.
├── combiner.py
├── mapper.py
├── new_genres.txt
├── new_ratings.txt
├── new_years.txt
├── ratings.txt
├── r5.txt
├── r100.txt
├── reducer.py
├── runhadoop.sh
└── README.md
```

## Files

- **ratings.txt**: The main input file containing over 100,000 ratings.
- **r5.txt**: A smaller version of the ratings data containing 5 rows of data.
- **r100.txt**: A smaller version of the ratings data containing 100 rows of data.
- **years.txt**: Specifies the years to be analyzed.
- **genres.txt**: Specifies the genres to be analyzed.
- **mapper.py**: The mapper script.
- **combiner.py**: The combiner script.
- **reducer.py**: The reducer script.
- **runhadoop.sh**: Shell script to run the Hadoop job.
- **README.md**: This readme file.

## Input Files Format

### ratings.txt

Each line in the file contains an individual user's rating for a particular movie as follows:

```plaintext
ReviewerID MovieTitle Genres Year Rating
```

Example:

```plaintext
387   Kickboxer Action      1989 2.5
599   Lionheart Action      1990 0.5
599   Tornado!    Action      1996 2
599   Steel       Action      1997 1
217   Steel       Action      1997 3
140   Yojimbo     Action|Adventure 1961 1
23    Yojimbo     Action|Adventure 1961 3
```

### years.txt

Specifies the years to be analyzed. If empty, all years are analyzed.

Example:

```plaintext
1999
2009
2010
2014
```

### genres.txt

Specifies the genres to be analyzed. If empty, all genres are analyzed.

Example:

```plaintext
Action
Sci-Fi
```

## Running the MapReduce Job

You can simulate the MapReduce process locally by running the scripts and piping the outputs as follows:

```bash
# Run the mapper
cat new_ratings.txt | python3 mapper.py | sort > mapped_output.txt

# Use the mapped output as input for the combiner
cat mapped_output.txt | python3 combiner.py | sort > combined_output.txt

# Use the combined output as input for the reducer
cat combined_output.txt | python3 reducer.py
```

## Test Cases

 Here are some example test cases:

- **Basic Functionality**: Check if the scripts correctly process the sample data and produce the expected output.
- **Empty Years File**: Verify that the scripts analyze all years when `years.txt` is empty.
- **Empty Genres File**: Verify that the scripts analyze all genres when `genres.txt` is empty.
- **Edge Case - No Matching Year**: Ensure the scripts handle cases where `ratings.txt` contains none of the years listed in `years.txt`.
- **Edge Case - No Matching Genre**: Ensure the scripts handle cases where `ratings.txt` contains none of the genres listed in `genres.txt`.
- **Tie Case**: Verify that the scripts correctly handle cases where two or more movies have the same highest average rating for a year.


