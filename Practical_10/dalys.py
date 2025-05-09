import os # Import necessary libraries
import pandas as pd # Import pandas for data manipulation
import matplotlib.pyplot as plt # Import matplotlib for plotting
import numpy as np # Import numpy for numerical operations
os.chdir("Practical_10") # Change the working directory to the folder where the script is located
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # Read the CSV file

# Some tryings
'''
dalys_data.info() # Display information about the DataFrame
print(dalys_data.head(5)) # Display the first few rows of the dataset
print(dalys_data.iloc[0:2,0])# Display the first two rows of the first column
print(dalys_data.iloc[0:5:2,0:1])# Display every second row of the first column
'''

#code for showing the third column for the first 10 rows
print(dalys_data.iloc[0:10,2]) 

'The tenth year  with DALYs data recorded in Afghanistan is 1999 '
'and data is 82624.94'

#The DALYs for countries in 1990
print('\nThe DALYs for countries in 1990')
print(dalys_data[dalys_data.Year==1990][['Entity','DALYs']]) # Display the DALYs for all countries in 1990

# mean DALYs in the UK and France
Uk=dalys_data[dalys_data.Entity== 'United Kingdom'] 
France=dalys_data[dalys_data.Entity== 'France'] # Filter the data for the UK and France
mean_Uk=Uk['DALYs'].mean() # Calculate the mean DALYs for the UK
mean_France=France['DALYs'].mean() # Calculate the mean DALYs for France
print('The mean DALYs in the UK is:',mean_Uk) # Print the mean DALYs for the UK
print('The mean DALYs in France is:',mean_France) # Print the mean DALYs for France
print('The mean DALYs in the UK is greater than France') 
'UK is greater than France'

#A plot showing the DALYS over time in the UK
Uk=dalys_data[dalys_data.Entity== 'United Kingdom'] # Filter the data for the UK
plt.plot(Uk['Year'],Uk['DALYs']) # Plot the DALYs over time in the UK
plt.title('DALYs in the UK over time') # Set the title of the plot
plt.xlabel('Year') # Set the x-axis label
plt.ylabel('DALYs') # Set the y-axis label
plt.show() # Display the plot

#code to answer the question stated in file question.txt
Afghanistan=dalys_data[dalys_data.Entity== 'Afghanistan' ] # Filter the data for Afghanistan
Afghanistan_70000=Afghanistan[Afghanistan['DALYs']>70000] # Filter the data for DALYs greater than 70000
print('The years in which the DALYs in Afghanistan were greater than 70000 are:',Afghanistan_70000['Year'].values) # Display the years with DALYs greater than 70000
print('The DALYs in Afghanistan in 1990 is:',len(Afghanistan_70000)) # Display the number of years with DALYs greater than 70000 in 1990