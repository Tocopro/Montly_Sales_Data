
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = df ['month_number'].to_list()
faceCreamSalesData = df['facecream'].to_list()
faceWashSalesData = df['facewash'].to_list()

plt.bar([a-0.25 for a in monthList], faceCreamSalesData, width=0.25, label='Face Cream Sales Data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width=-0.35, label='Face Wash Sales Data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle='--')
plt.title('Facewash and facecream sales data')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
month_list = df ['month_number'].to_list()
bathingSoapSalesData = df ['bathingsoap'].to_list()
plt.bar(month_list, bathingSoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.title('Sales Data')
plt.xticks(month_list)
plt.grid(True, linewidth=1, linestyle="--")
plt.title('bathingsoap sales data')
plt.savefig('C:\\Users\\NEAK\\Downloads\\company_sales_data.png', dpi=150)
plt.show()


df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
profitList = df ['total_profit'].to_list()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label= 'Profit Data')
plt.xlabel('Profit range in Dollars')
plt.ylabel('Actual Profit in Dollars')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit Data')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = df['month_number'].to_list()

labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(),
             df['shampoo'].sum(),
             df['moisturizer'].sum()]
plt.axis('equal')
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales Data')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = df['month_number'].to_list()
bathingSoap = df['bathingsoap'].to_list()
faceWashSalesData = df['facewash'].to_list()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingSoap, label='Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of a Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label='FaceWash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales Data of a FaceWash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = df['month_number'].to_list()

faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot([], [], color='m', label='face Cream', linewidth=5)
plt.plot([], [], color='c', label='Face wash', linewidth=5)
plt.plot([], [], color='r', label='Tooth paste', linewidth=5)
plt.plot([], [], color='k', label='Bathing soap', linewidth=5)
plt.plot([], [], color='g', label='Shampoo', linewidth=5)
plt.plot([], [], color='y', label='Moisturizer', linewidth=5)

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, bathingsoapSalesData,
              shampooSalesData,
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData, colors=['m', 'c', 'r', 'k', 'g', 'y'])

plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.title('All products sales data using stack plot')
plt.legend(loc='upper right')
plt.show()

