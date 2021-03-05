#Visualize Twitch Data with Matplotlib
#Now that you’ve conducted some analysis with SQL, you will be taking your findings from the SQL queries and visualize them using Python and Matplotlib, in the forms of:
#Bar Graph: Featured Games
#Pie Chart: Stream Viewers’ Locations
#Line Graph: Time Series Analysis

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)),viewers, color='red')
plt.xlabel('Game')
plt.ylabel('Number of Viewers')
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation = 25)
plt.title('Featured Games on Twitch')
plt.show()

plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

plt.title('League of Legends Viewer Location')
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries, colors = colors, explode= explode,shadow= True, startangle = 345, labels= labels,autopct = '%1.0f%%', pctdistance= .75)
plt.axis('equal')
plt.show()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.clf()

y_upper = [i * 1.15 for i in viewers_hour]
y_lower = [i * .85 for i in viewers_hour]
plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_lower,y_upper, alpha = .2)
plt.title('Twitch Viewers on January 1,2015')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Viewers')
ax = plt.subplot()
ax.set_xticks(hour)
plt.show()

