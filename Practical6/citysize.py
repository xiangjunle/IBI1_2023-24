uk_population=[0.56,0.62,0.04,9.7] 
china_population=[0.58,8.4,29.9,22.2]
uk_cities=['Edinburgh','Glasgow','Stirling','London']
china_cities=['Haining','Hangzhou','Shanghai','Beijing']
uk={}
china={}
for key, value in zip(uk_population,uk_cities):
    uk[key]=value
uk_population.sort()
for i in range(len(uk_population)):
    print(uk[uk_population[i]]) 
    print(uk_population[i])
print("the	list of	sorted	values of china is below")
for key, value in zip(china_population,china_cities):
    china[key]=value
china_population.sort()
for i in range(len(china_population)):
    print(china[china_population[i]]) 
    print(china_population[i])
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
ax.bar(uk_cities, uk_population, label=uk_cities, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()
plt.clf()


