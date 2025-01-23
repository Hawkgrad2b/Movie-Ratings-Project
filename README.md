# Movie-Ratings-Project
# Movie Recommendation System Project

## Overview

This project involves building a simple movie recommendation system using a dataset of 100,000 movie ratings collected by the GroupLens Research Group at the University of Minnesota. It introduces basic concepts in machine learning by implementing functions to process and analyze data, as well as providing visualizations for demographic-based preferences. The project also includes simple algorithms to predict user ratings.

## Dataset

The dataset, collected via the MovieLens website, contains:
- **User demographics** (e.g., age, gender, occupation, zip code).
- **Movie details** (e.g., title, release date, genres).
- **Ratings** (user, movie, rating).

The data is pre-cleaned, with incomplete entries removed.

### Key Files
- `u.data`: Ratings data.
- `u.info`: Dataset summary.
- `u.item`: Movie metadata.
- `u.genre`: Movie genres.
- `u.user`: User demographics.
- `u.occupation`: Occupation codes.

The dataset is available at [MovieLens 100k](http://files.grouplens.org/datasets/movielens/ml-100k.zip).

---

## Phase 1: Data Processing & Visualization

### Tasks
1. **Create Data Structures**  
   - User list, movie list, ratings list, and genre list are generated using Python functions.
2. **Explore the Dataset**  
   - A function analyzes ratings based on user demographics (age, gender) and genres.
3. **Visualizations**  
   - Use Matplotlib to create bar plots comparing:
     - Male vs. Female preferences.
     - Younger (20-30) vs. Older (50-60) adults’ preferences.  
   - Plots are created for 5 genres: Action, Comedy, Drama, Horror, Romance.

---

## Phase 1 Deliverables

1. **Python Files**
   - `project2Phase1a.py`: Data processing functions (autograded).
   - `project2Phase1b.py`: Main program to generate plots.
2. **PDF File**
   - `plots.pdf`: Contains 4 labeled and color-coded bar plots.

---

## Prediction Algorithms

Simple algorithms for predicting user ratings include:
1. **Random Prediction**: Random integer rating (1-5).
2. **Mean User Rating**: Mean rating a user has given.
3. **Mean Movie Rating**: Mean rating a movie has received.
4. **Mean Rating**: Average of the user’s mean rating and the movie’s mean rating.

---

## Requirements

- **Programming Language**: Python
- **Libraries**: 
  - [Matplotlib](https://matplotlib.org/) for visualizations.
  - Standard libraries for file I/O and data manipulation.

---

## Instructions

1. **Dataset Setup**  
   Download and extract the dataset. Focus on the six files mentioned above.
   
2. **Run the Code**
   - Use `project2Phase1b.py` to generate plots.
   - Analyze the results in `plots.pdf`.

3. **Future Work**  
   Phases 2-3 will introduce collaborative filtering for enhanced recommendations.

---

This project offers an introduction to machine learning and data analysis through recommender systems. Explore how user demographics and preferences shape movie ratings while gaining hands-on experience with Python and visualization tools.
