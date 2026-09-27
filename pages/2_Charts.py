import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.set_page_config(page_title="Charts")

st.sidebar.header("Charts")

df = pd.read_csv("data.csv")

#Group the data by getting the mean of anxiety, depression, ocd, and insomnia for fav genre
df_grouped = df.groupby("Fav genre")[["Anxiety", "Depression", "OCD", "Insomnia"]].mean().round(2)

#Check for how often different age groups listen to music per day
age_bracket_list = []

for age in df["Age"]:
  #filter out the extreme value for 24 hours per day of music
  if age >= 10 and age < 20:
    age_bracket_list.append("10 - 20")
  elif age >= 20 and age < 30:
    age_bracket_list.append("20 - 30")
  elif age >= 30 and age < 40:
    age_bracket_list.append("30 - 40")
  elif age >= 40 and age < 50:
    age_bracket_list.append("40 - 50")
  elif age >= 50 and age < 60:
    age_bracket_list.append("50 - 60")
  elif age >= 60 and age < 70:
    age_bracket_list.append("60 - 70")
  elif age >= 70 and age < 80:
    age_bracket_list.append("70 - 80")
  else:
    age_bracket_list.append("80+")

df["Age Bracket"] = age_bracket_list
df_remove_extreme = df[df["Hours per day"] < 24]
df_age_bracket = df_remove_extreme.groupby("Age Bracket")[["Hours per day" , "Anxiety", "Depression", "OCD", "Insomnia"]].mean().round(2)

#Check for the different ages and their favorite genres
df_age_genre = df.groupby("Fav genre")[["Age"]].mean().round(0)

#Determine the effect of favorite genres on people's wellbeing
df_music_effect_group_percentages = pd.crosstab(df["Fav genre"], df["Music effects"], normalize = 'index').round(2) #normalize everything to 1.0 scale to make it a percentage
sorted_percentages = df_music_effect_group_percentages.sort_values("Improve", ascending = False) #Make the highest improvement genre display at the top

#Bar charts
#Use streamlit run Charts.py in the terminal
age_grouped_anxiety = df.groupby("Age Bracket")["Anxiety"].mean().reset_index() #Resetting the index makes sure the length of both lists is the same
st.bar_chart(data = age_grouped_anxiety, x = "Age Bracket", y = "Anxiety")

age_grouped_depression = df.groupby("Age Bracket")["Depression"].mean().reset_index() #Resetting the index makes sure the length of both lists is the same
st.bar_chart(data = age_grouped_depression, x = "Age Bracket", y = "Depression")

age_grouped_ocd = df.groupby("Age Bracket")["OCD"].mean().reset_index() #Resetting the index makes sure the length of both lists is the same
st.bar_chart(data = age_grouped_ocd, x = "Age Bracket", y = "OCD")

age_grouped_insomnia = df.groupby("Age Bracket")["Insomnia"].mean().reset_index() #Resetting the index makes sure the length of both lists is the same
st.bar_chart(data = age_grouped_insomnia, x = "Age Bracket", y = "Insomnia")