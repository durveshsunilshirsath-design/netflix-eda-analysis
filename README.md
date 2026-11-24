# Netflix Movies and TV Shows – Exploratory Data Analysis

## Project Overview
This project explores the Netflix Movies and TV Shows dataset using Python to identify patterns and trends in the content available on Netflix.

## Objectives
- Understand the dataset structure.
- Identify and handle missing values.
- Check duplicate records.
- Analyse Movies vs TV Shows.
- Explore country-wise content distribution.
- Analyse content ratings.
- Study release-year trends.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

## Analysis Performed
1. Data loading and inspection
2. Missing value analysis
3. Duplicate checking and removal
4. Content type distribution
5. Country distribution
6. Content rating vs content type
7. Release year analysis

## Project Structure
- `EDA.py` – Python analysis script
- `data/` – Dataset folder
- `requirements.txt` – Required Python libraries

## How to Run
1. Clone or download this repository.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Place the dataset at `data/netflix_titles.csv`.
4. Run:
   `python EDA.py`

## Key Findings
1. **Content Type:** The dataset contains 6,131 Movies (69.6%) and 2,676 TV Shows (30.4%), showing that Movies make up the larger share of Netflix content.

2. **Top Countries:** The United States has the highest number of country entries (2,818), followed by India (972) and the United Kingdom (419).

3. **Content Ratings:** TV-MA is the most common rating, with 3,207 titles, followed by TV-14 with 2,160 titles.

4. **Rating vs Content Type:** Both Movies and TV Shows have TV-MA as their most common rating. The dataset contains 2,062 TV-MA Movies and 1,145 TV-MA TV Shows.

5. **Release Year:** 2018 has the highest number of titles, with 1,147 releases, followed by 2017 (1,032) and 2019 (1,030).

## Conclusion
This project demonstrates the use of Python and Pandas for data cleaning, exploration and basic data visualisation.

## Author
**Durvesh**  
BCA Student | Aspiring Data Analyst
Interested in Data Analytics, Python, and Data Visualization.
