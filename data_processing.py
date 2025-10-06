"""
This project is designed to answer a few questions :
1. Which opponent have Arsenal played the most times?
2. Against which opponent do Arsenal have the highest and lowest win rate?
3. Against which opponent do Arsenal have the highest non-loss rate? 
   - Are these the same as Q2?
4. How many countries have Arsenal’s opponents come from?
5. Against which opponent do Arsenal have the best and worst goal difference?
   — Does the best goal difference equal the highest win rate?
6. Against which opponent do Arsenal have the highest points per match (PPM)?
   — Does the highest PPM equal the highest win rate?

Questions 2,4,5 will only take into account opponents that Arsenal have played 
at least 5 times.
"""

import pandas as pd
df = pd.read_csv("arsenal_h2h_records.csv")
df = df.drop("Head-to-Head", axis=1)
df['Country'] = df['Country'].astype(str).str.strip().str.split(r'\s+', n=1).str[1]
# print(df.shape) # check number of rows and columns
# print(df.isna().any()) # check if any values are missing
# print(df.dtypes) 
# print(df.head())

## Question 1
idx = df["MP"].idxmax()
highest_MP = df.loc[idx, "MP"]
highest_MP_team = df.loc[idx, "Squad"]
print(f"Q1: Arsenal have played {highest_MP_team} the most, a total of {highest_MP} times\n")


## Question 2
df["Win Rate"] = round(df["W"] / df["MP"], 4)
win_rate_df = df[df["MP"] >= 5]

high_idx = win_rate_df["Win Rate"].idxmax()
highest_WR = win_rate_df.loc[high_idx, "Win Rate"] * 100
highest_WR_teams_df = win_rate_df[win_rate_df["Win Rate"] == 1]
highest_WR_teams = highest_WR_teams_df["Squad"].values
highest_WR_teams = ", ".join(highest_WR_teams)

low_idx = win_rate_df["Win Rate"].idxmin()
lowest_WR = win_rate_df.loc[low_idx, "Win Rate"] * 100
lowest_WR = round(lowest_WR, 2)
lowest_WR_team = win_rate_df.loc[low_idx, "Squad"]

print(f"Q2: Arsenal have the highest win rate of {highest_WR}% against {highest_WR_teams} and the lowest win rate of {lowest_WR}% against {lowest_WR_team}\n")
print(win_rate_df.sort_values(by="Win Rate", ascending=False))
print("\n")


## Question 3
df["Non-Lose Rate"] = round((df["W"] + df["D"]) / df["MP"], 4)
non_lose_df = df[df["MP"] >= 5]

idx = non_lose_df["Non-Lose Rate"].idxmax()
highest_NLR = non_lose_df.loc[idx, "Non-Lose Rate"] * 100
highest_NLR_teams_df = non_lose_df[non_lose_df["Non-Lose Rate"] == 1]
highest_NLR_teams = highest_NLR_teams_df["Squad"].values
highest_NLR_teams = ", ".join(highest_NLR_teams)

print(f"Q3: Arsenal have the highest non-lose rate of {highest_NLR}% against {highest_NLR_teams}\n")
print(non_lose_df.sort_values("Non-Lose Rate", ascending=False))
print("\n")


## Question 4
unique_country = df["Country"].nunique() 
print(f"Q4: Arsenal's opponents have come from {unique_country} different countries, below shows a list of the number of teams from each country :\n")

countries_count = df["Country"].value_counts()

countries = []
for country in countries_count.index:
    countries.append(country)

country_count = countries_count.values.tolist() # convert numpy array to a list
counts = []
for count in country_count:
    counts.append(count)

country_count_list = list(zip(countries, counts))
print(f"{country_count_list}\n")


## Question 5
GD_df = df[df["MP"] >= 5]
high_idx = GD_df["GD"].idxmax()
highest_GD = GD_df.loc[high_idx, "GD"]
highest_GD_team = GD_df.loc[high_idx, "Squad"]

low_idx = GD_df["GD"].idxmin()
lowest_GD = GD_df.loc[low_idx, "GD"]
lowest_GD_team = GD_df.loc[low_idx, "Squad"]

print(f"Q5: Arsenal have the highest goal difference of {highest_GD} against {highest_GD_team} and the lowest goal difference of {lowest_GD} against {lowest_GD_team}\n")


## Question 6
PPM_df = df[df["MP"] >= 5]
print("Q6: First table shows the table sorted by PPM; second table shows the table sorted by Win Rate. Although the difference isn't huge, a high PPM doesn't always equal high win rate\n")
print(PPM_df.sort_values("PPM", ascending=False).head(10))
print("\n")
print(PPM_df.sort_values("Win Rate", ascending=False).head(10))