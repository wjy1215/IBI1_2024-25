import matplotlib.pyplot as plt
languages_dic = {'JaveScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, 'TypeScript': 38.5}
plt.bar(languages_dic.keys(), languages_dic.values())
plt.title('Popular Programming Languages')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.show()
print(languages_dic.get('HTML')) #Change the value of the key to be displayed