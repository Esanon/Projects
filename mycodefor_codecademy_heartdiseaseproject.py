# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

sns.boxplot(x= heart.thalach, y= heart.heart_disease)
plt.show()

thalach_hd = heart.thalach[heart.heart_disease == 'presence' ]
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence' ]

thalach_hd_mean = np.mean(thalach_hd)
thalach_no_hd_mean = np.mean(thalach_no_hd)
print(thalach_hd_mean - thalach_no_hd_mean)

tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
#pval is less than .05 so there is significance and null hypothesis is rejected and alternative hypothesis that the average thalach for a person with heart disease is not equal to the average thalach for a person with heart disease. 
plt.clf()
sns.boxplot(x= heart.age, y= heart.heart_disease)
plt.show()

plt.clf()
sns.boxplot(x= heart.chol, y= heart.heart_disease)
plt.show()

plt.clf()
sns.boxplot(x= heart.trestbps, y= heart.heart_disease)
plt.show()

plt.clf()
sns.boxplot(x= heart.thalach, y= heart.cp)
plt.show()

thalach_typical = heart.thalach[heart.cp == 'typical angina' ]
thalach_atypical= heart.thalach[heart.cp == 'atypical angina' ]
thalach_nonagin = heart.thalach[heart.cp == 'non-anginal pain' ]
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic' ]

Fstat, pval = f_oneway(thalach_typical, thalach_nonagin, thalach_atypical,thalach_asymptom )
print(pval)
#pval is less than .05 so it is significant. reject null, accept alternative that People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach. 
results = pairwise_tukeyhsd(heart.thalach, heart.cp)
print(results)

xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(xtab)
#The majority of people with heart diseases had asymptomatic chest pain
chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)
#less than .05. significant association between heart disease and type of chest pain