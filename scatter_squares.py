import matplotlib.pyplot as plt

#plotting a series of points using scatter()
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig,ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,s=20)

#set chart title and label axes
ax.set_title("Square Numbers",fontsize = 24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of value",fontsize=14)

#set size of tick labels
ax.tick_params(axis='both',which='major',labelsize=14)

#set the range for each axis
ax.axis([0,1100,0,110])

plt.show()

