import pandas as pd

df = pd.read_csv("data/netflix_titles.csv")

print(df.info())
print(df.columns)
print("==================================================")


# How many Movies vs TV Shows are on Netflix?
print(df["type"].value_counts())
movies_count = df["type"].value_counts()
movies_per = (movies_count["Movie"]/(movies_count.sum()))*100
print(f"Movies account for {round(movies_per, 2)}% of total netflix content till 2021-09-25.")
print("==================================================")

# Which countries produce the most content?
country = df["country"].dropna().str.split(", ").explode()
country = country.value_counts()
print(country.index[0],":",country.iloc[0])
print("Out of 127 countries United states has",round((country.iloc[0]/country.sum())*100,2),"% of country-title associations.")
print("==================================================")

# Which years produced most Movies and TV Shows?
release_yr = df["release_year"].value_counts().sort_values(ascending=False)
growth = release_yr.diff()
print(growth.index[0],"Has produced most Movies and TV Shows.")
print("==================================================")

# Which genres are most common?
genres = df["listed_in"].dropna().str.split(", ").explode()
genres = genres.value_counts().sort_values(ascending=False)
print("Common Genres on Netflix")
for i in range(3):
    print(genres.index[i], ":", genres.iloc[i])
print("==================================================")

# What is the average movie duration?
movies = df[df["type"] == "Movie"].copy()
movies["duration"] = movies["duration"].str.replace(" min","",regex=True)
movies["duration"] = pd.to_numeric(movies["duration"])
print("Average Movie Duration: ",round(movies["duration"].mean(numeric_only=True), 2))
print("==================================================")

# Which directors appear most often?
directors = df["director"].dropna().str.split(", ").explode()
director_count = directors.value_counts()
print("Director which appears most often is",
      director_count.index[0],
      "with",
      director_count.iloc[0],"titles.")
print("==================================================")

# What content is added most recently?
df["date_added"] = pd.to_datetime(df["date_added"], format= "%B %d, %Y",errors="coerce")
latest_content = df[df["date_added"] == df["date_added"].max()]
print("Content most recently added is:")
print(latest_content[
    ["title","type","date_added"]
])
print("==================================================")