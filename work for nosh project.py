#The Nosh Mish Mosh is a recipe and ingredient meal delivery service. They ship the raw materials and you get to cook them at your home! They’ve decided to hire a data analyst to help make product and interface decisions. Get started to help them figure out the amount of data they’ll need to make meaningful decisions.

#We’ve collected customer data for the past week and exposed it through a Python library, so first import noshmishmosh

import noshmishmosh 
import numpy as np

#Nosh Mish Mosh wants to run an experiment to see if we can convince more people to purchase meal plans if we use a more artisanal-looking vegetable selection. We’ve photographed these modern meals with blush tomatoes and graffiti eggplants, but aren’t sure if this strategy will sell enough units to benefit from establishing a business relationship with a new provider.

#Before running this experiment, of course, we need to know the sample size that will be required to detect the difference we are hoping for. There are three things we need to know before we can determine that number.the Baseline Conversion RateMinimum Detectable Effect (desired lift)and the Statistical Significance Threshold

all_visitors = noshmishmosh.customer_visits 
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = paying_visitor_count/ total_visitor_count * 100
print("Baseline Percent: " + str(baseline_percent))

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)

new_customers_needed = np.ceil(1240/average_payment)
print(new_customers_needed)

percent_point_increase = new_customers_needed/total_visitor_count * 100
print(percent_point_increase)

mde = percent_point_increase/baseline_percent * 100
print("Minimum Detectable Effect: "+ str(mde))

#significance threshold = 10%, baseline = 18.6, mde = 50.5...input into sample size calculator

ab_sample_size = 490 