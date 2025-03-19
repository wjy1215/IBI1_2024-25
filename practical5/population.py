#input: 57.11,3.13,1.91,5.45
#output: [57.11,5.45,3.13,1.91]
#input: 65.77,41.88,45.28,61.27,85.15
#output: [85.15,65.77,61.27,45.28,41.88]
# Create a pie chart to show the population distribution of the UK and China
# Create a variable to store the population of the UK and China 
# Create a variable to store the countries and provinces
# import the matplotlib library
import matplotlib.pyplot as plt 
uk_population=[57.11,3.13,1.91,5.45]
countries=['England','Scotland','Wales','Northern Ireland']
china_population=[65.77,41.88,45.28,61.27,85.15]
provience=['Zhejiang','Fujiang','Jiangxi','Hanhui','Jiangsu']
sorted_UK= sorted(uk_population,reverse=True)
sorted_China= sorted(china_population,reverse=True) 
print(sorted_UK)
print(sorted_China)
plt.pie(sorted_UK,labels=countries,autopct='%1.2f%%')
plt.title('UK Population Distribution')
plt.show()
plt.pie(sorted_China,labels=provience,autopct='%1.2f%%')
plt.title('China Population Distribution')
plt.show()
