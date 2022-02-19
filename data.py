#%%
# Import Pandas according to the 
# conventional method. Then load the dataset into a Pandas dataframe.
import pandas as pd
# Write any code needed to explore the data by seeing what the first few 
# rows look like. Then display a technical summary of the data to determine
# the data types of each column, and which columns have missing data.
dat = pd.read_csv("https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/titanic.csv")
dat.head(5)
# dat.describe

# %%
# Write the code needed to generate visualizations that explain gender, survival rate, siblings vs 
# & spouses

import altair as alt

survive_chart = alt.Chart(dat).mark_bar().encode(
    alt.X('Survived'),
    alt.Y('count()')
)

gender_chart = alt.Chart(dat).mark_bar().encode(
    alt.X('Sex'),
    alt.Y('count()')
)

sibsp_chart = alt.Chart(dat).mark_bar().encode(
    alt.X('SibSp'),
    alt.Y('count()')
)

parch_chart = alt.Chart(dat).mark_bar().encode(
    alt.X('Parch'),
    alt.Y('count()')
)

# survive_chart
# gender_chart
sibsp_chart
# parch_chart

#%%
# Write code to explore how different features in the data affect the survival distribution

class_chart = alt.Chart(dat).mark_bar().encode(
    alt.Y('count(Pclass)'),
    alt.X('Pclass'),
    alt.Color('Survived')
)

sex_chart = alt.Chart(dat).mark_bar().encode(
    alt.Y('count(Sex)'),
    alt.X('Sex'),
    alt.Color('Survived')
)

age_chart = alt.Chart(dat).mark_bar().encode(
    alt.Y('count(Age)'),
    alt.X('Age'),
    alt.Color('Survived')
)
sex_chart
#age_chart
#class_chart

#%%
# create two new columns
dat["Name"].str.lower()
dat["Surname"] = dat["Name"].str.split(",").str.get(0)
dat["Name"].str.contains("Countess")
dat[dat["Name"].str.contains("Countess")]

####
#NETLFIX
# %%
# Part 2: Load the dataset into a Pandas dataframe.
netflix = pd.read_csv("https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/netflix_titles.csv")
# Then, explore the data by seeing what the first few rows look like. 
netflix.head(5)

#%%
# Next, display a technical summary of the data to determine the data types of each column, and which columns have missing data.
netflix.info()

#%%
# Use pandas's filtering abilitites to select the subset of data
# that represents movies, then calculate how many rows are in the filtered data.
netflix_movies = netflix[netflix["type"] == "Movie"]
len(netflix_movies)

#%%
# Determine the number of records for each value of the "rating" feature.
# Remember to count the values in your subset only, not in the original dataframe.
netflix_movies['rating'].value_counts()

#%%
# Filter the list of movies to select a new subset containing only movies with
# a standard MPAA rating. Calculate how many rows are in this new set, and
# then see which ratings appear most often.
movies_MPAA = netflix_movies[(netflix_movies['rating'] == 'G') | (netflix_movies['rating'] == 'PG') | (netflix_movies['rating'] == 'PG-13') | (netflix_movies['rating'] == 'R') | (netflix_movies['rating'] == 'NC-17')]
movies_MPAA
