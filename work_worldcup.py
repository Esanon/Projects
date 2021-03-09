#For this project you will be exploring data from the Fifa World Cup from 1930-2014 to analyze trends and discover insights about the world’s game, fútbol! This Fifa World Cup data is from Kaggle. Kaggle is a platform for data science competitions that hosts many datasets online.
#Using Seaborn you will create a series of plots that explore aggregates and distribution across the goals scored in World Cup games.

#import modules
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#create dataframe 
df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

#create new column for total goals 
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

#create bar chart for total goals. style = whitegrid 
sns.set_style('whitegrid')
sns.set_context('poster', font_scale = .7)
f,ax = plt.subplots(figsize=(12,7))
sns.barplot(data = df, x='Year', y='Total Goals')
ax.set_title('Average Number of Goals during the World Cup')
plt.show()

#create a data frame for goals 
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())


#create a boxplot for df_goals 
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1.25)
f,ax2 = plt.subplots(figsize=(12,7))
sns.boxplot(data = df_goals, x='year', y='goals', palette= 'Spectral')
ax2.set_title('Goals per year')
plt.show()