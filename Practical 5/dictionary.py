#create a dictionary of programming languages and their popularity
#display the popularity of the selected language
#change the selected language to see the popularity
# import the matplotlib library
#change lables to keys and autopct to values
# show the bar chart
import matplotlib.pyplot as plt
languages_dic = {'JavaScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, 'TypeScript': 38.5}
print(languages_dic)
plt.bar(languages_dic.keys(), languages_dic.values())
plt.title('Popular Programming Languages')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.show()
selected_language = 'HTML' # Change the language to see the popularity
print(languages_dic[selected_language]) #Display the value of the key
