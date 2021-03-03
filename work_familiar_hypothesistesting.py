#Welcome to Familiar, a startup in the new market of blood transfusion! You’ve joined the team because you appreciate the flexible hours and extremely intelligent team, but the overeager doorman welcoming you into the office is a nice way to start your workday (well, work-evening).Familiar has fallen into some tough times lately, so you’re hoping to help them make some insights about their product and help move the needle (so to speak)

# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
#Use the .head() method to print out the first five rows and take a look!

print(lifespans.head(5))

#The first thing we want to know is whether Familiar’s most basic package, the Vein Pack, actually has a significant impact on the subscribers. It would be a marketing goldmine if we can show that subscribers to the Vein Pack live longer than other people. Extract the life spans of subscribers to the 'vein' pack and save the data into a variable called vein_pack_lifespans.

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
print(vein_pack_lifespans.head())

#Next, use np.mean() to calculate the average lifespan for Vein Pack subscribers and print the result. Is it longer than 73 years?

print(np.mean(vein_pack_lifespans))
#mean = 76.17

#We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 73 years.Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:
#Null: The average lifespan of a Vein Pack subscriber is 73 years.
#Alternative: The average lifespan of a Vein Pack subscriber is NOT 73 years.

#will use 1-sample t-test. imported at the top. sample to quantitative comparison. 

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)
#result 5.972157921433082e-07. Less than .05 - significant. Reject null hypothesis. Accept the alternative. average lifespan of a vein pack suscriber is not 73 years. 

#Let’s get the lifespans of Artery Pack subscribers. Using the same lifespans dataset, extract the lifespans of subscribers to the Artery Pack and save them as artery_pack_lifespans

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
print(artery_pack_lifespans.head())


#Use np.mean() to calculate the average lifespan for Artery Pack subscribers and print the result. Is it longer than for the Vein Pack?

print(np.mean(artery_pack_lifespans))
#result : 74.8736622351704

#We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack.Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

#Null: The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber.
#Alternative: The average lifespan of a Vein Pack subscriber is NOT equal to the average lifespan of an Artery Pack subscriber.

#binary vein vs artery and lifespan is quantitative. using a 2-sample t-test. imported at the top. 

tstat, pval = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
print(pval)
#pval = 0.05588883079070819 slightly above .05 results not significant. accept null hypothesis and average lifespans are not significantly different. 

#The Familiar team has provided us with another dataset containing survey data about iron counts for our subscribers. This data has been pre-processed to categorize iron counts as “low”, “normal”, and “high” for each subscriber. Familiar wants to be able to advise potential subscribers about possible side effects of these packs and whether they differ for the Vein vs. the Artery pack.

print(iron.head())

#Is there an association between the pack that a subscriber gets (Vein vs. Artery) and their iron level? Use the pandas crosstab() function to create a contingency table of the pack and iron columns in the iron data. Save the result as Xtab and print it out

Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

#We’d like to find out if there is a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level.Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

#Null: There is NOT an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.
#Alternative: There is an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.

#testing assocations between binary variables and qualitative data. Will run chi-square test. imported above. 

chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
#result: 9.359749337433008e-25
#significant finding. reject null. accept alternate hypothesis that there is an association between subscription pack and iron level. 