#In this project, you’ll analyze data from the NBA (National Basketball Association) and explore possible associations.

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba_2010.fran_id == 'Knicks']
nets_pts = nba_2010.pts[nba_2010.fran_id == 'Nets']

diff_means_2010 = np.mean(knicks_pts) - np.mean(nets_pts)
print(diff_means_2010)

plt.hist(knicks_pts, alpha = .8, normed = True, label = 'Knicks')
plt.hist(nets_pts, alpha = .8, normed = True, label = 'Nets')
plt.legend()
plt.show()

knicks_pts_2 = nba_2014.pts[nba_2014.fran_id == 'Knicks']
nets_pts_2 = nba_2014.pts[nba_2014.fran_id == 'Nets']
diff_means_2014 = np.mean(knicks_pts_2) - np.mean(nets_pts_2)
print(diff_means_2014)

plt.clf()
plt.hist(knicks_pts_2, alpha = .8, normed = True, label = 'Knicks')
plt.hist(nets_pts_2, alpha = .8, normed = True, label = 'Nets')
plt.legend()
plt.show()

plt.clf()
sns.boxplot(data =nba_2010, x=nba_2010.fran_id, y=nba_2010.pts)
plt.show()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(cov)

correlation, p =pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(correlation)

plt.clf()
plt.scatter(x= nba_2010.forecast, y=nba_2010.point_diff)
plt.xlabel('Forecast')
plt.ylabel("Point Difference")
plt.show()