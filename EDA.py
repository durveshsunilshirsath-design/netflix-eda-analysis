# Netflix Movies and TV Shows - Exploratory Data Analysis
# -------------------------------------------------------
# Libraries used: Pandas, NumPy and Matplotlib
# Dataset: netflix_titles.csv
#
# Folder structure:
# Netflix-EDA/
#     EDA.py
#     data/
#         netflix_titles.csv
#
# Run this file from the main Netflix-EDA folder.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. LOAD THE DATASET
df = pd.read_csv("data/netflix_titles.csv")


# 2. UNDERSTANDING THE DATASET

print("\nFIRST 10 ROWS")
print(df.head(10))

print("\nDATASET SHAPE (ROWS, COLUMNS)")
print(df.shape)

print("\nDATASET INFORMATION")
df.info()

print("\nSTATISTICAL SUMMARY")
print(df.describe(include="all"))

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())


# 3. DATA CLEANING

# Fill missing values in these columns with 'Unknown'.
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# Remove duplicate rows, if any.
df = df.drop_duplicates()

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nDATASET SHAPE AFTER CLEANING")
print(df.shape)


# 4. ANALYSIS 1 - MOVIES VS TV SHOWS

content_type = df["type"].value_counts()

print("\nMOVIES VS TV SHOWS")
print(content_type)

content_type.plot(kind="bar", figsize=(7, 5))
plt.title("Distribution of Netflix Content Type")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 5. ANALYSIS 2 - TOP 10 COUNTRIES

country_count = df["country"].value_counts().head(10)

print("\nTOP 10 COUNTRY ENTRIES")
print(country_count)

country_count.plot(kind="bar", figsize=(10, 5))
plt.title("Top 10 Countries by Content Count")
plt.xlabel("Country entry")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Note:
# Some rows contain more than one country, for example:
# "India, United States". In this basic analysis, that full combination
# is counted as one entry. We can improve this later using split() and explode().


# 6. ANALYSIS 3 - CONTENT RATING VS CONTENT TYPE

result = pd.crosstab(df["rating"], df["type"])

print("\nCONTENT RATING VS CONTENT TYPE")
print(result)

result.plot(kind="bar", figsize=(12, 6))
plt.title("Content Rating vs Content Type")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# 7. ANALYSIS 4 - TITLES BY RELEASE YEAR

release_year_count = df["release_year"].value_counts().sort_index()

print("\nTITLES BY RELEASE YEAR")
print(release_year_count)

release_year_count.plot(kind="line", figsize=(12, 5))
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


# 8. ANALYSIS 5 - TOP 10 RELEASE YEARS BY TITLE COUNT

top_release_years = df["release_year"].value_counts().head(10)

print("\nTOP 10 RELEASE YEARS BY NUMBER OF TITLES")
print(top_release_years)

top_release_years.sort_index().plot(kind="bar", figsize=(10, 5))
plt.title("Top 10 Release Years by Number of Titles")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 9. FINAL OBSERVATIONS
print("\nFINAL DATASET SUMMARY")
print("Total number of titles:", len(df))
print("Total number of columns:", len(df.columns))
print("Number of Movies:", (df["type"] == "Movie").sum())
print("Number of TV Shows:", (df["type"] == "TV Show").sum())

print("\nEDA COMPLETED")
