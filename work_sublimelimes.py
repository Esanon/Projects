#Line Graph Project using matplotlib 
#Data Visualization module 

import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

#Create subplots with a figure width of 12 and height of 8. Plot total visits over the past year. Graphs as ax1 and ax2. Give line markers. Label x-axis, y-axis and include a title. Add x-axis ticks and x-axis tick labels. 

plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))
plt.xlabel('Months')
plt.ylabel('Montly Visits')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Monthly Customer Purchases')
plt.plot(x_values, visits_per_month, marker ='*')
plt.savefig('Subplot1.png')

#Plot three lines on the same set of axes. Each line is the various lime datas vs months. Specify the color. Add a legend. Set x-axis ticks and tick labels. Save figures as png files. 

ax2= plt.subplot(1,2,2)
plt.plot(x_values,key_limes_per_month, color = 'green', label = 'Key Limes')
plt.plot(x_values, persian_limes_per_month, color = 'red', label = 'Persian Limes')
plt.plot(x_values, blood_limes_per_month, color = 'blue', label = 'Blood Limes')
plt.legend(loc = 1)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Breakdown by Lime Type')
plt.savefig('Subplot2.png')

plt.subplots_adjust(bottom = .5)
plt.show()
