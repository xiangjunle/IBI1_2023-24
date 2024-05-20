x={'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'Other':3.5}
import matplotlib.pyplot as plt
class_labels = ["Sleeping", "Classes", "Studying", "TV", "Music", "Other"]
time_week = [8, 6, 3.5, 2, 1, 3.5]
plt.figure()
plt.pie(time_week, labels =class_labels, startangle = 24)
fig, ax = plt.subplots()
ax.pie(time_week, labels=class_labels, autopct='%1.1f%%')
plt.show()
plt.clf() 
print(x) 
 