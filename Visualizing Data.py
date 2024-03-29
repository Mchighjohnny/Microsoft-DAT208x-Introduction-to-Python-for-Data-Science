

##Plotting Scatterplots

# Import matplotlib
import matplotlib.pyplot as plt
# Create scatter plot
plt.scatter(unemployment_rate, low_wage_jobs)
# Label x axis
plt.xlabel('Unemployment rate')
# Label y axis
plt.ylabel('Low pay jobs')
# Display the graph 
plt.show()


##Modifying Plot Colors
# Plot the red and triangle shaped scatter plot  
plt.scatter(unemployment_rate, low_wage_jobs, color="r", marker='^')
# Display the visualization
plt.show()


##Plotting Histograms
# Plot a histogram of sharewomen
plt.hist(sharewomen)
# Show the plot
plt.show()


##Plotting with pandas
# Import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Create scatter plot
dept_stats.plot(kind='scatter', x='unemployment_rate', y='low_wage_jobs')
plt.show()


##Plotting One Bar Graphs
# DataFrame of non-college job sums
df = recent_grads.groupby(['major_category']).non_college_jobs.sum()
# Plot bar chart
df.plot(kind='bar')
# Show graph
plt.show()



##Plotting Two Bar Graphs
# DataFrame of college and non-college job sums
df1 = recent_grads.groupby(['major_category'])['college_jobs','non_college_jobs'].sum()
# Plot bar chart
df1.plot(kind="bar")
# Show graph
plt.show()


##Dropping Missing Values
# Print the size of the DataFrame
print(recent_grads.size)
# Drop all rows with a missing value
recent_grads.dropna(axis=0,inplace=True)
# Print the size of the DataFrame
print(recent_grads.size)




##Plotting Quantiles of Salary, Part 1
# Convert to numeric and divide by 1000
recent_grads['median'] = pd.to_numeric(recent_grads['median'])/1000
recent_grads['p25th'] = pd.to_numeric(recent_grads['p25th'])/1000
recent_grads['p75th'] = pd.to_numeric(recent_grads['p75th'])/1000

# 
columns = ['median', 'p25th', 'p75th']
sal_quantiles = recent_grads.groupby(['major_category'])[columns].mean()


##Plotting Quantiles of Salary, Part 2
# Plot the data
sal_quantiles.plot()
# Set xticks
plt.xticks(np.arange(len(sal_quantiles.index)),sal_quantiles.index,rotation='vertical')
# Show the plot
plt.show()
# Plot with subplots
sal_quantiles.plot(subplots=True)
plt.show()
