#Brian is a Product Manager at FarmBurg, a company that makes a farming simulation social network game. In the FarmBurg game, you can plow, plant, and harvest different crops. ​Brian has been conducting an A/B Test with three different variants, and he wants you to help him analyze the results. Using the Python modules pandas and SciPy, you will help him make some important business decisions!

# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency 
from scipy.stats import binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

print(abdata.head())

#Note that we have two categorical variables: group and is_purchase. We are interested in whether visitors are more likely to make a purchase if they are in any one group compared to the others. 

Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
#Group A has highest number of purchases 

chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
#result: 2.4126213546684264e-35. well below .05 so there is a significant different between group purchase rates. 

#New prompt: Brian has added pricepoints for each group. "What we really want to know is whether each price point allows us to make enough money that we can exceed some target goal." Pricepoint: minimum $1000 revenue/ week. Need to calculate necessary purchase rate for each price point. 

num_visits = len(abdata.user_id)
print(num_visits)
#4998 weekly visitors on the game. 

#Now that we know how many visitors we generally get each week (num_visits), we need to calculate the number of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99) in order to generate Brian’s minimum revenue target of $1,000 per week.

num_sales_needed_099 = 1000/ .99
print(num_sales_needed_099)
#results 1011 sales 

#Now that we know how many sales we need at a $0.99 price point, calculate the proportion of weekly visitors who would need to make a purchase in order to meet that goal. Remember that the number of weekly visitors is saved as num_visits. Save the result as p_sales_needed_099 and print it out.

p_sales_needed_099 = num_sales_needed_099 / num_visits
print(p_sales_needed_099)
#results 20.2% 

#Repeat the steps from tasks 5 and 6 for the other price points ($1.99 and $4.99). Save the number of sales needed for each price point as num_sales_needed_199 and num_sales_needed_499, respectively. Then, save the proportion of visits needed as p_sales_needed_199 and p_sales_needed_499, respectively

num_sales_needed_199 = 1000/ 1.99
print(num_sales_needed_199)
#503 sales needed
p_sales_needed_199 = num_sales_needed_199 / num_visits
print(p_sales_needed_199)
#10%

num_sales_needed_499 = 1000/ 4.99
print(num_sales_needed_499)
#201 sales needed
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(p_sales_needed_499)
# 4%

#Now let’s return to Brian’s question. To start, we want to know if the percent of Group A (the $0.99 price point) that purchased an upgrade package is significantly greater than p_sales_needed_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our minimum revenue target of $1,000).

samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

#Calculate the sample size and number of purchases in group B (the $1.99 price point) and save them as samp_size_199 and sales_199, respectively. Then do the same for group C (the $4.99 price point) and save them as samp_size_499 and sales_499, respectively.

samp_size_199 =np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499= np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

#For Group A ($0.99 price point), perform a binomial test using binom_test() to see if the observed purchase rate is significantly greater than p_sales_needed_099

pvalueA = binom_test(x= sales_099, n =samp_size_099, p= p_sales_needed_099,alternative='greater')
print(pvalueA)
#pvalue = .9 so observed purchased rate at 99 cents is not significantly greater than the minimum revenue target purchase rate. 


pvalueB = binom_test(x= sales_199, n =samp_size_199, p= p_sales_needed_199,alternative='greater')
print(pvalueB)
#pvalue = .11 so observed purchased rate at $1.99 is not significantly greater than the minimum revenue target purchase rate.

pvalueC = binom_test(x= sales_499, n =samp_size_499, p= p_sales_needed_499,alternative='greater')
print(pvalueC)
#pvalue = .02 so the observed purchased rate at $4.99 is significantly greater than the minimum revenue target purchase rate. Brian will charge $4.99 for the upgrade. 