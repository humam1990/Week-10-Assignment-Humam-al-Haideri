"""
***********************************************************

Description: Week-10 Assignment
		     Idea : Using matplotlib to show a pie chart
		     graph of the value distribution of different stocks 
		     
             
Humam Al-Haideri

Revision: 6/7/2019
"""
#importing required modules and libraries.

import matplotlib.pyplot as plt
import matplotlib


labels = ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB', 'M', 'F', 'IBM']
c_prices = [941.53, 73.04, 55.74, 65.27, 172.54, 23.98, 10.95, 145.3]

#Creating pie chart.
plt.pie(c_prices, labels = labels)
plt.title("Daily Stock Rates", fontsize=20)	
plt.ylabel("Stock Value in US Dollar", fontsize=10)	
plt.legend()
plt.savefig('Stock Rates.png', bbox_inches='tight')	
plt.show()

