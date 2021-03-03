#Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up prospective dog owners with their perfect pet. FetchMaker has been collecting data on their adoptable dogs, and it’s your job to analyze some of that data.

# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

print(dogs.head(10))

#FetchMaker estimates (based on historical data for all dogs) that 8% of dogs in their system are rescues.They would like to know if whippets are significantly more or less likely than other dogs to be a rescue.Store the is_rescue values for 'whippet's in a variable called whippet_rescue.

whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']

#How many whippets are rescues (remember that the value of is_rescue is 1 for rescues and 0 otherwise)? Save this number as num_whippet_rescues and print it out.

num_whippet_rescues = np.sum(whippet_rescue)
print(num_whippet_rescues)
#6 rescues are whippets

#How many whippets are in this sample of data in total? Save this number as num_whippets and print it out
num_whippets = len(whippet_rescue)
print(num_whippets)
#result : 100

#Use a hypothesis test to test the following null and alternative hypotheses:Null: 8% of whippets are rescues. Alternative: more or less than 8% of whippets are rescues. Save the p-value from this test as pval and print it out. Using a significance threshold of 0.05, Is the proportion of whippets who are rescues significantly different from 8%?

#sample to categorical variable - binomial test. imported above

p_value = binom_test(6, n=100, p=0.08)
print(p_value)
#result .58 - proportion of rescue whippets not significantly different from 8%

#Three of FetchMaker’s most popular mid-sized dog breeds are 'whippet's, 'terrier's, and 'pitbull's. Is there a significant difference in the average weights of these three dog breeds?To start answering this question, save the weights of each of these breeds in three separate series named wt_whippets, wt_terriers, and wt_pitbulls, respectively.

wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

#Run a single hypothesis test to address the following null and alternative hypotheses:
#Null: whippets, terriers, and pitbulls all weigh the same amount on average
#Alternative: whippets, terriers, and pitbulls do not all weigh the same amount on average (at least one pair of breeds has differing average weights)
#Save the resulting p-value as pval and print it out. Using a significance threshold of 0.05, is there at least one pair of dog breeds that have significantly different average weights?

Fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)
#result 3.276415588274815e-17 - less than .05. at least one pair has significant average weight differences. Need to run tukey's range test. 

tukey_results = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print(tukey_results)
#reject is true for 2/3 pairs. reject the null and accept alternative hypothesis. significant weight difference between pitbull and terriers and between terriers and whippets. 

#FetchMaker wants to know if 'poodle's and 'shihtzu's come in different colors.To start, use the subsetted data to create a contingency table of dog colors by breed (poodle vs. shihtzu). Save the table as Xtab and print it out.

Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(Xtab)

#Run a hypothesis test for the following null and alternative hypotheses:
#Null: There is an association between breed (poodle vs. shihtzu) and color.
#Alternative: There is not an association between breed (poodle vs. shihtzu) and color.
#Save the p-value as pval and print it out. Do poodles and shihtzus come in significantly different color combinations? Use a significance threshold of 0.05.

chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)

#result .005 so findings are significant enought to reject null. There isn't a signification association between color and breed.